import re

def all_ints_inclusive(nums):
    s = set(re.findall('(?<=333)[0-9]+', nums))
    s.update(re.findall('(?<=368)[0-9]+', nums))
    return list(s)