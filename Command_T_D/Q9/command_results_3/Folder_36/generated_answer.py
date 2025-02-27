import re

def all_odd_ints_inclusive(nums):
    str_nums = ' '.join((str(x) for x in nums))
    return re.findall('odd', str_nums)