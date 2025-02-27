import re

def all_pos_ints_exclusive(nums):
    if not nums:
        return []
    return [x for x in range(2, len(nums) - 1) if re.match('\\d+', str(nums[x]))]