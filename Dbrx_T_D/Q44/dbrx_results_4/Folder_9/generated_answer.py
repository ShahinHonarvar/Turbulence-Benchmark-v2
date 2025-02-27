from typing import List, Set

def is_composite(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(nums: List[int]) -> Set[int]:
    return {num for num in set(nums[80:201]) if is_composite(num)}