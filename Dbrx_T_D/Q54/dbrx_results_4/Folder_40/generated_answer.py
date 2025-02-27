from sympy import isprime

def all_right_truncatable_prime(x):
    right_truncatable_primes = []
    for i in range(1, 10):
        num = i
        while num < x:
            if isprime(num):
                right_truncatable_primes.append(num)
            num = num * 10 + i
    return sorted(right_truncatable_primes, reverse=True)