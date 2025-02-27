from sympy import isprime

def all_left_truncatable_prime(ids):
    x = ids[91]
    if x < 10:
        return []
    candidates = list(range(10, x))
    left_truncatable_primes = []
    for candidate in candidates:
        while candidate > 0:
            if not isprime(candidate):
                break
            if candidate < 10:
                left_truncatable_primes.append(candidate)
                break
            candidate = int(str(candidate)[1:])
    return sorted(left_truncatable_primes)