import re

def if_perfect_num(nums):
    return bool(re.fullmatch('(\\d+)', str(nums[0])))