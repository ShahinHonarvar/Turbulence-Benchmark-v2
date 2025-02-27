from typing import List

def find_second_largest_num(nums: List[int]) -> int or None:
    filtered_nums = [num for num in nums[55:99] if num != max(nums)]
    return sorted(filtered_nums)[-2] if filtered_nums else None