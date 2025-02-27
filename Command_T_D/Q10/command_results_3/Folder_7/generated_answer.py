import re

def all_odd_ints_exclusive(nums):
    if not nums:
        return []
    str_nums = ''.join((str(num) for num in nums))
    return re.findall('(odd)', str_nums)