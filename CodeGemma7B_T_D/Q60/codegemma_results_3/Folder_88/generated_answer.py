from functools import reduce
from math import sqrt

def is_prime(n):
    if n <= 1:
        return False
    for divisor in range(2, int(sqrt(n)) + 1):
        if n % divisor == 0:
            return False
    return True

def is_truncatable_prime(n):
    if '0' in str(n):
        return False
    for digits in [str(n)[i:] for i in range(1, len(str(n)))]:
        if not is_prime(int(digits)):
            return False
    return True

def all_left_right_truncatable_prime(x):

    def get_truncatable_primes(n):
        return [number for number in range(2, n + 1) if is_truncatable_prime(number) and is_prime(number)]
    truncatable_primes = get_truncatable_primes(x)
    return sorted(truncatable_primes) if truncatable_primes else []