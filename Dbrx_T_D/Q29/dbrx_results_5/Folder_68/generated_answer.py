from functools import reduce

def gcf_two_nums(nums):
    x, y = (nums[8], nums[9])
    if x == 0:
        return y
    while y != 0:
        x, y = (y, x % y)
    return x