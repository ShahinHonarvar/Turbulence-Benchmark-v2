import math
from functools import reduce

def gcf_three_nums(nums):
    return reduce(math.gcd, (nums[944], nums[814], nums[865]))