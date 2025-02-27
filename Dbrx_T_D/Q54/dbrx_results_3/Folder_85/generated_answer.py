from sympy import isprime

def all_right_truncatable_prime(indices):
    x = indices[94]
    primes = [i for i in range(2, x) if isprime(i)]
    right_primes = []
    for p in primes:
        s = str(p)
        while len(s) > 1 and isprime(int(s)):
            s = s[:-1]
        if len(s) == 1:
            right_primes.append(p)
    return sorted(list(set(right_primes)))