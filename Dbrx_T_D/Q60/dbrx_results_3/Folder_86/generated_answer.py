import itertools
from sympy import isprime

def all_left_right_truncatable_prime(bounds):
    x = bounds[0] if len(bounds) == 1 else bounds[126]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    result = []
    for p in primes:
        p_str = str(p)
        if '0' in p_str:
            continue
        for i in range(1, len(p_str)):
            if not isprime(int(p_str[i:])):
                break
            if not isprime(int(p_str[:-i])):
                break
        else:
            result.append(p)
    return sorted(result, reverse=True)