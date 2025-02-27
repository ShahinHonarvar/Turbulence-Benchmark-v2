def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    num1 = nums[44]
    num2 = nums[91]
    num3 = nums[42]
    return gcd(gcd(num1, num2), num3)