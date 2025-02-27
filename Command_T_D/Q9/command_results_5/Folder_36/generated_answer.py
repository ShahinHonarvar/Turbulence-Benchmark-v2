import re

def all_odd_ints_inclusive(nums):
    return re.findall('( odd)?\\d+', nums[246:750 + 1])