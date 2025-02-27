def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    num1 = nums[64]
    num2 = nums[80]
    num3 = nums[15]
    return gcd(gcd(num1, num2), num3)