import re

def all_left_right_truncatable_prime(n):
    s = str(n)
    return sorted((x for x, y in PRIMES if y <= n), reverse=True)