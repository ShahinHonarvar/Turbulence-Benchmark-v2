from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[14]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    ltrunc_primes = [p for p in primes if all((isprime(int(str(p)[i:])) for i in range(1, len(str(p)))))]
    rtrunc_primes = [p for p in primes if all((isprime(int(str(p)[:-i])) for i in range(1, len(str(p)))))]
    lrtrunc_primes = [p for p in ltrunc_primes if p in rtrunc_primes]
    return sorted(lrtrunc_primes)