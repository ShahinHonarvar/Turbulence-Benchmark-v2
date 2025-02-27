def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 1) == 0:
            return False
        i += 2
    return True

def truncate_left(n):
    while n > 9:
        n //= 10
        if not is_prime(n):
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[100]
    primes = []
    for i in range(2, x):
        if is_prime(i) and truncate_left(i):
            primes.append(i)
    primes.sort(reverse=True)
    return primes