from functools import lru_cache
from itertools import combinations_with_replacement, count

@lru_cache(maxsize=50000)
def is_prime(number):
    return all((number % divisor != 0 for divisor in range(2, int(number ** 0.5) + 1)))

@lru_cache(maxsize=50000)
def is_truncatable_prime(number):
    str_number = str(number)
    if '0' in str_number or str_number[0] == '0' or str_number[-1] == '0':
        return False

    def is_prime_for_digits(number):
        if number <= 2:
            return False
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                return False
        return True
    for i in range(len(str_number)):
        left = int(str_number[:i + 1])
        right = int(str_number[i:])
        if not (is_prime(left) and is_prime_for_digits(right)):
            return False
    return True

def all_left_right_truncatable_prime(tuple_range):
    x = tuple_range[70]
    left_right_truncatable_primes = []
    for number in range(2, x + 1):
        if is_truncatable_prime(number):
            left_right_truncatable_primes.append(number)
    return sorted(left_right_truncatable_primes, reverse=True) or []