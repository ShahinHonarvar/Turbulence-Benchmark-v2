from itertools import islice

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def truncate_left_and_right(n):
    if n < 10:
        return []
    primes = []
    while n > 0:
        if is_prime(n):
            primes.append(n)
        n //= 10
    return primes

def all_left_right_truncatable_prime(t):
    x = t[64]
    primes = []
    for i in range(2, x + 1):
        if is_prime(i) and len(truncate_left_and_right(i)) == i:
            primes.append(i)
    primes.sort(reverse=True)
    return primes