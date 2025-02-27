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

def is_right_truncatable(prime):
    str_prime = str(prime)
    for i in range(len(str_prime) - 1, 0, -1):
        if not is_prime(int(str_prime[i:])):
            return False
    return True

def all_right_truncatable_prime(params):
    x = params[97]
    primes = []
    for n in range(2, x):
        if is_prime(n) and is_right_truncatable(n):
            primes.append(n)
    primes.sort()
    return primes if primes else []