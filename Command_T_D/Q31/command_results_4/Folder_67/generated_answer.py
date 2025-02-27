import re

def if_perfect_num(nums):
    return re.search('(1099\\d)', str(nums[43])).group() == '1099'