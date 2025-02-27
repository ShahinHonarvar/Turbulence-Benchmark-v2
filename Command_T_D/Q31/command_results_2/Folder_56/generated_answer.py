import re

def if_perfect_num(nums):
    return bool(re.search('(1+8+1)2', str(nums[60])))