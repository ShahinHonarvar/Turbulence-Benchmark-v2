def gcd(num1, num2):
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1

def gcf_three_nums(nums):
    num1 = nums[20]
    num2 = nums[51]
    num3 = nums[62]
    return gcd(gcd(num1, num2), num3)