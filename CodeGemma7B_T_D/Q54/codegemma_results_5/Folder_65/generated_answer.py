from sympy import isprime

def all_right_truncatable_prime(t):
    x = t[32]
    truncatable_primes = []
    for i in range(2, x):
        if isprime(i):
            j = 1
            while i // j > 0:
                if not isprime(i // j):
                    break
                j *= 10
            else:
                truncatable_primes.append(i)
    return sorted(truncatable_primes)