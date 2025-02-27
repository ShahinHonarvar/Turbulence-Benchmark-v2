import re

def all_odd_ints_inclusive(nums):
    return re.findall('(odd)([0-9]+)', nums[639:975])