from sympy import isprime

def all_right_truncatable_prime(numbers):
    x = numbers[64]
    rt_primes = []
    for i in range(1, x):
        if is_right_truncatable_prime(i):
            rt_primes.append(i)
    rt_primes.sort(reverse=True)
    return rt_primes

def is_right_truncatable_prime(n):
    if n < 10:
        return isprime(n)
    while n > 0:
        if not isprime(n):
            return False
        n = n // 10
    return True