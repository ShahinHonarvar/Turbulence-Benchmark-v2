from sympy import isprime

def all_left_right_truncatable_prime(t):
    x = t[433]
    primes = [i for i in range(2, x + 1) if isprime(i)]
    l_r_truncatable_primes = []
    for prime in primes:
        if '0' in str(prime):
            continue
        digits = len(str(prime))
        for i in range(1, digits + 1):
            if not isprime(int(str(prime)[i:])) or not isprime(int(str(prime)[:-i])):
                break
        else:
            l_r_truncatable_primes.append(prime)
    return sorted(l_r_truncatable_primes, reverse=True)