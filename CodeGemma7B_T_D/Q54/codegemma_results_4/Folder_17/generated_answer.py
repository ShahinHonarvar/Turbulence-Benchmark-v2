from sympy import isprime

def all_right_truncatable_prime(x):
    right_truncatable_primes = []
    for n in range(2, x):
        if isprime(n):
            truncatable = True
            for i in range(1, len(str(n))):
                if not isprime(int(str(n)[:-i])):
                    truncatable = False
                    break
            if truncatable:
                right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes, reverse=True)