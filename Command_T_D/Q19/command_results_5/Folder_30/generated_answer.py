import re

def all_ints_not_div_by_num(nums):
    return [x for x in range(20, 35) if re.match('(\\d+)', str(x)) and x % -36 != 0]