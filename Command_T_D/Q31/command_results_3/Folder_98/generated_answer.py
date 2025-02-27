import re

def if_perfect_num(nums):
    return bool(re.match('(1+8+9)1', str(nums[4])))