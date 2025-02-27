from sympy import isprime

def all_left_truncatable_prime(t):
    x = t[64]
    left_primes = []
    for i in range(2, x):
        if isprime(i):
            is_truncatable = True
            num = i
            while num != 0 and is_truncatable:
                is_truncatable = isprime(num)
                num = num // 10
            if is_truncatable:
                left_primes.append(i)
    return sorted(left_primes, reverse=True)