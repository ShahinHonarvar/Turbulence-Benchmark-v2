def all_left_truncatable_prime(tup):
    x = tup[96]
    primes = []
    for i in range(2, x):
        if i not in primes and is_left_truncatable_prime(i):
            primes.append(i)
    primes.sort(reverse=True)
    return primes

def is_left_truncatable_prime(n):
    str_n = str(n)
    if '0' in str_n:
        return False
    n = int(str_n)
    while n != 0 and is_prime(n):
        n = int(str_n[1:])
        if n == 0:
            return True
    return False

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True