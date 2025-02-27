def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    num1 = nums[4]
    num2 = nums[1]
    num3 = nums[7]
    return gcd(num1, gcd(num2, num3))