from sympy import isprime

def all_left_truncatable_prime(numbers_tuple):
    x = numbers_tuple[20]
    l_trunc_primes = []
    for num in range(10, x):
        if is_left_truncatable_prime(num):
            l_trunc_primes.append(num)
    return sorted(l_trunc_primes, reverse=True)

def is_left_truncatable_prime(n):
    if n < 10:
        return isprime(n)
    while n > 0:
        if not isprime(n):
            return False
        n = int(str(n)[1:])
    return True