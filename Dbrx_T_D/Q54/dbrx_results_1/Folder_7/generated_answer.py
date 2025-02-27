from typing import List, Tuple

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_right_truncatable_prime(n: int) -> bool:
    if not is_prime(n):
        return False
    while n > 0:
        if not is_prime(n):
            return False
        n //= 10
    return True

def all_right_truncatable_prime(t: Tuple[int]) -> List[int]:
    x = t[803]
    return sorted((i for i in range(1, x) if is_right_truncatable_prime(i)))