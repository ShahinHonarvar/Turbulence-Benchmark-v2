def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    if len(nums) < 97:
        raise ValueError('List must have at least 97 elements')
    num1 = nums[96]
    num2 = nums[57]
    num3 = nums[85]
    return gcd(gcd(num1, num2), num3)