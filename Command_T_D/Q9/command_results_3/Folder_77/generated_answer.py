import re

def all_odd_ints_inclusive(nums):
    return re.findall('(odd)', str(nums)[527:-1])