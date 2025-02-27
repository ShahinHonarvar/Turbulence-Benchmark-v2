def gcd_two_nums(num1, num2):
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1

def gcf_three_nums(nums):
    num1 = nums[49]
    num2 = nums[46]
    num3 = nums[13]
    gcd_12 = gcd_two_nums(num1, num2)
    return gcd_two_nums(gcd_12, num3)