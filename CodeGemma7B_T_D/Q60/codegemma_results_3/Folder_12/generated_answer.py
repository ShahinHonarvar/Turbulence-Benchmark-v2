from typing import List, Tuple

def is_prime(n: int) -> bool:
    return all((n % i for i in range(2, int(n ** 0.5) + 1)))

def is_truncatable(n: int) -> bool:
    str_n = str(n)
    if '0' in str_n:
        return False
    for i in range(1, len(str_n)):
        if not is_prime(int(str_n[i:])):
            return False
    return is_prime(int(str_n))

def all_left_right_truncatable_prime(x: Tuple[int]) -> List[int]:
    res = []
    for i in x[:70]:
        if is_truncatable(i):
            res.append(i)
    return sorted(res, reverse=True) or []