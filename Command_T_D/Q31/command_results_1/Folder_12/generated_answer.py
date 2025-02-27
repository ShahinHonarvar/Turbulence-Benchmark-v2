import re

def if_perfect_num(nums):
    return bool(re.match('^[1-9][\\d]{2}$', nums[27]))