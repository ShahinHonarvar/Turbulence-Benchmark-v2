def gcf_two_nums(nums):
    return gcd(nums[60], nums[64])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a