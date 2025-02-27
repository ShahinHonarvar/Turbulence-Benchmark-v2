from typing import List

def all_ints_not_div_by_num(nums: List[int]) -> List[int]:
    indices = range(8, 9)
    result = [num for i, num in enumerate(nums) if i not in indices and num % 8 != 0]
    if not result:
        result = []
    return result