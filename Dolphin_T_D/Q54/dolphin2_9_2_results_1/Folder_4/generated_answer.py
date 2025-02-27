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

def is_right_truncatable(n):
    str_n = str(n)
    for i in range(len(str_n) - 1):
        if not is_prime(int(str_n[i:])):
            return False
    return True

def all_right_truncatable_prime(arg):
    x = arg[96]
    primes = []
    for i in range(x):
        if is_prime(i) and is_right_truncatable(i):
            primes.append(i)
    return sorted(primes, reverse=True) if primes else []