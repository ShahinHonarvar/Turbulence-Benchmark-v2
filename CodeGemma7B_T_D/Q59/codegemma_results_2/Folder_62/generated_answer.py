from itertools import count
import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(t):
    x = t[70]
    primes = [n for n in count(2) if is_prime(n)]
    result = []
    for p in primes:
        if p < x and (not str(p).startswith('0')):
            truncated_primes = [p]
            for i in range(1, len(str(p))):
                truncated_primes.append(int(str(p)[i:]))
            if all((is_prime(p) for p in truncated_primes)):
                result.append(p)
    return sorted(result)