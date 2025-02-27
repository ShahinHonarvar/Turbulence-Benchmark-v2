from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[177]
    primes = list(range(2, x + 1))
    primes = [p for p in primes if isprime(p)]
    l_r_truncatable_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        s = str(prime)
        while s:
            if not isprime(int(s)):
                break
            s = s[1:] if len(s) > 1 else []
            if s and (not isprime(int(s))):
                break
            s = s[:-1] if s else []
        else:
            l_r_truncatable_primes.append(prime)
    return sorted(l_r_truncatable_primes)