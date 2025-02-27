import itertools
import re

def all_left_truncatable_prime(tup):
    x, = tup
    primes = itertools.permutations(range(2, x))
    if 0 in primes:
        return []
    if 1 in primes:
        return [2]
    if 2 in primes:
        return [3]
    if 3 in primes:
        return [5]
    if 5 in primes:
        return [7]
    if 6 in primes:
        return [11]
    if 7 in primes:
        return [13]
    if 8 in primes:
        return [17]
    if 9 in primes:
        return [19]
    if 4 in primes:
        return [5]
    if 3 in primes:
        return [5]
    if 2 in primes:
        return [3]
    if 1 in primes:
        return [2]
    if 0 in primes:
        return []
    if not primes:
        return []
    left_truncatable_primes = []
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)
    left_truncatable_primes.sort(reverse=True)