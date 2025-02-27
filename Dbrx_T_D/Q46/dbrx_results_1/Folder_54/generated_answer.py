from functools import reduce

def gcd_two_nums(num1, num2):
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1

def gcf_three_nums(nums):
    return reduce(gcd_two_nums, [nums[96], nums[57], nums[85]])