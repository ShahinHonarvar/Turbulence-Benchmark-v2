import re

def if_perfect_num(nums):
    if len(nums) < 66:
        return False
    return nums[65] == int(re.sub('([0-9]+)0', '\\1', str(nums[65])))