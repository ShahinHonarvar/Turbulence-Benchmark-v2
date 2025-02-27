from typing import List

def is_composite(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(nums: List[int]) -> set:
    composite_nums = {n for n in nums[50:55] if is_composite(n)}
    return composite_nums