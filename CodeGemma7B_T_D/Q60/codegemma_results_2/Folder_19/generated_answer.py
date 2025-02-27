from typing import List, Tuple

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def left_truncatable_prime(num: int) -> bool:
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[i:])):
            return False
    return True

def right_truncatable_prime(num: int) -> bool:
    str_num = str(num)
    if '0' in str_num:
        return False
    for i in range(1, len(str_num)):
        if not is_prime(int(str_num[:-i])):
            return False
    return True

def all_left_right_truncatable_prime(nums: Tuple[int, ...]) -> List[int]:
    result = []
    for num in nums:
        if left_truncatable_prime(num) and right_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result