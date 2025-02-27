import math

def all_left_truncatable_prime(n):
    return [n for n in range(3, int(math.ceil(math.sqrt(n)) + 1) + 1) if is_left_truncatable_prime(str(n))]