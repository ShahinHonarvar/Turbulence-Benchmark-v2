import sympy

def all_right_truncatable_prime(t):
    x = t[85]
    primes = []
    for num in range(2, x):
        if sympy.isprime(num):
            truncation = num
            while truncation:
                truncation //= 10
                if not sympy.isprime(truncation):
                    break
            else:
                primes.append(num)
    return sorted(primes)