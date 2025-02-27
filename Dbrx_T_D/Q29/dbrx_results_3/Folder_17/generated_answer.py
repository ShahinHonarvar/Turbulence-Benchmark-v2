import math

def gcf_two_nums(nums):
    num1 = nums[69]
    num2 = nums[40]
    factor = 2
    smallest_num = min(num1, num2)
    gcf = 1
    while factor <= smallest_num:
        if num1 % factor == 0 and num2 % factor == 0:
            gcf = factor
        factor += 1
    return gcf