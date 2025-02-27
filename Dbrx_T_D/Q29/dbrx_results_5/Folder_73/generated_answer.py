import math

def gcf_two_nums(nums):
    num1 = nums[51]
    num2 = nums[27]
    factor = int(math.sqrt(num1 * num2))
    while num1 % factor != 0 or num2 % factor != 0:
        factor -= 1
    return factor