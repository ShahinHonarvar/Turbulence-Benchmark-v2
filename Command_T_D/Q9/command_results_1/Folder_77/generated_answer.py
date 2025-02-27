import re

def all_odd_ints_inclusive(nums):
    return re.findall('(odd){:d}{:d}(:odd){:d}{:d}(:odd){:d}{:d}(odd){:d}{:d}', str(nums))