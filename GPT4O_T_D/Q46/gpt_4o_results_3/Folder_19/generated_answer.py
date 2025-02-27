import math
from functools import reduce

def gcf_three_nums(nums):

    def gcf(a, b):
        return math.gcd(a, b)
    selected_nums = [nums[40], nums[15], nums[99]]
    return reduce(gcf, selected_nums)