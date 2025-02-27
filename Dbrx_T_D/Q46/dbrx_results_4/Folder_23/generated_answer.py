def gcd_two_nums(num1, num2):
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1

def gcf_three_nums(nums):
    num1 = nums[31]
    num2 = nums[25]
    num3 = nums[80]
    return gcd_two_nums(gcd_two_nums(num1, num2), num3)