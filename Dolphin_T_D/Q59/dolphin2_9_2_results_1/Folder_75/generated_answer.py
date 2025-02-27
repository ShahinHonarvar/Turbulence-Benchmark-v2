def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def left_trunc(n):
    while n > 0 and n % 10 == 0:
        n //= 10
    return is_prime(n)

def all_left_truncatable_prime(x):
    primes = []
    for n in range(2, x):
        if left_trunc(n):
            primes.append(n)
    return sorted(primes)