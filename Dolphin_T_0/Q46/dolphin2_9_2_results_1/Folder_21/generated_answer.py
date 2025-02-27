def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcd(gcd(nums[412], nums[932]), nums[337])