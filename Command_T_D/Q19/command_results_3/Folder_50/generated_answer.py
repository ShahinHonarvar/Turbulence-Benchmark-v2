import re

def all_ints_not_div_by_num(nums):
    return [x for x in nums[13:76] if not re.fullmatch('44\\*', str(x))]