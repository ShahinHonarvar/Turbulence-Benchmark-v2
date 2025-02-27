import re

def all_odd_ints_exclusive(nums):
    return re.findall('(odd)([0-9]+)', str(range(15, 99)))