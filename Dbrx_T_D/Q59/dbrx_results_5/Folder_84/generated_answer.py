import sympy

def all_left_truncatable_prime(nums_tuple):
    x = nums_tuple[630]
    primes = [i for i in range(2, x) if sympy.isprime(i)]
    left_truncatable_primes = []
    for prime in primes:
        s = str(prime)
        for i in range(1, len(s)):
            if not sympy.isprime(int(s[i:])):
                break
        else:
            left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes, reverse=True)