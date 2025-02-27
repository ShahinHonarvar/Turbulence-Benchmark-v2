from sympy import isprime

def all_left_right_truncatable_prime(tup):
    primes = [i for i in range(2, tup[93] + 1) if isprime(i)]
    l_trunc_prime = [p for p in primes if all((isprime(int(str(p)[i:])) for i in range(1, len(str(p)))))]
    lr_trunc_primes = [p for p in l_trunc_prime if all((isprime(int(str(p)[:-i])) for i in range(1, len(str(p)))))]
    return sorted(lr_trunc_primes)