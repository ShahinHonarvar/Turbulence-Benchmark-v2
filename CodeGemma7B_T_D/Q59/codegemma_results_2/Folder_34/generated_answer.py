from math import sqrt

def all_left_truncatable_prime(t):
    x = t[17]
    truncatable_primes = []
    for n in range(2 ** 16, x):
        if is_prime(n) and has_no_zero(n):
            if is_all_prime_after_removal(n):
                truncatable_primes.append(n)
    truncatable_primes.sort(reverse=True)
    return truncatable_primes

def has_no_zero(n):
    return '0' not in str(n)

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

def is_all_prime_after_removal(n):
    for i in range(len(str(n)) - 1):
        number = int(str(n)[i + 1:])
        if not is_prime(number):
            return False
    return True