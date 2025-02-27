def gcd_two_nums(num1, num2):
    while num2:
        num1, num2 = (num2, num1 % num2)
    return abs(num1)

def gcf_three_nums(nums):
    return gcd_two_nums(gcd_two_nums(nums[40], nums[68]), nums[27])