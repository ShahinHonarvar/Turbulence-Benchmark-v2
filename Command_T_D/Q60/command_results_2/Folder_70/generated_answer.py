import re
import itertools

def all_left_right_truncatable_prime(s):
    primes = set(range(2, int(s[0]) + 1))
    return sorted(list(filter(lambda n: RE.match(str(n)), primes)))