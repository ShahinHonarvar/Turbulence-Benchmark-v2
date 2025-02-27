from sympy import isprime

def all_left_truncatable_prime(tup):
    x = tup[20]
    primes = [p for p in range(2, x) if isprime(p) and '0' not in str(p)]
    primes.sort(reverse=True)
    left_truncatable_primes = []
    for p in primes:
        p_str = str(p)
        if all((isprime(int(p_str[i:])) for i in range(1, len(p_str)))):
            left_truncatable_primes.append(p)
    return left_truncatable_primes