import sys

def all_pos_ints_exclusive(nums):
    indices = range(40, 200, 1)
    if indices not in nums:
        return []
    else:
        return [nums[i] for i in indices]