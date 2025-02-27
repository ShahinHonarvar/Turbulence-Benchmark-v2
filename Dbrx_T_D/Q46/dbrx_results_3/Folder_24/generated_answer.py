def gcd_two_nums(num1, num2):
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1

def gcf_three_nums(nums):
    return gcd_two_nums(nums[18], gcd_two_nums(nums[37], nums[43]))