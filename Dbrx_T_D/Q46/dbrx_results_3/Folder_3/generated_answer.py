import math

def gcf_three_nums(nums):
    elem1, elem2, elem3 = (nums[31], nums[69], nums[40])
    gcf_computation = math.gcd(elem1, elem2)
    gcf_final = math.gcd(gcf_computation, elem3)
    return gcf_final