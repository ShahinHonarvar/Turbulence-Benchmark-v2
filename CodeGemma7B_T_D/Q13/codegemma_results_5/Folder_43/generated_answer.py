from typing import List

def find_second_largest_num(numbers: List[int]) -> int:
    if not numbers or len(numbers) < 69 or max(numbers[:69]) == max(numbers[68:87]):
        return None
    sorted_nums = sorted(numbers[68:87], reverse=True)
    return sorted_nums[1] if len(sorted_nums) > 1 else None