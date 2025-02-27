from typing import List, Tuple
from math import sqrt

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable_prime(n: int) -> bool:
    if not is_prime(n) or '0' in str(n):
        return False
    for i in range(len(str(n)) // 2 + 1):
        if not is_prime(int(str(n)[i:])) or not is_prime(int(str(n)[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(limit_tuple: Tuple[int, ...]) -> List[int]:
    limit = max(limit_tuple)
    if limit < 11:
        return []
    result = []
    for i in range(11, limit + 1):
        if is_left_and_right_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)