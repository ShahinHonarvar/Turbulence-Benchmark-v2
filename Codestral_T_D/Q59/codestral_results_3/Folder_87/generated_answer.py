from itertools import combinations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[39]
    primes = [p for p in range(2, x) if is_prime(p)]
    left_truncatable_primes = []
    for p in primes:
        digits = [int(d) for d in str(p)]
        if 0 not in digits:
            truncated = [int(''.join(map(str, d))) for d in combinations(digits, len(digits) - 1) if d[0] != 0]
            if all((is_prime(t) for t in truncated)):
                left_truncatable_primes.append(p)
    return sorted(left_truncatable_primes, reverse=True)