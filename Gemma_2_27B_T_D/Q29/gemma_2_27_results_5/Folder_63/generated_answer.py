def gcf_two_nums(nums):
    return gcd(nums[21], nums[17])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a