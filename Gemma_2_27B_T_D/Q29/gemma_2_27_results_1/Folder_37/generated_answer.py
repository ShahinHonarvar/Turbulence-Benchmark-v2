def gcf_two_nums(nums):
    return gcd(nums[29], nums[74])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a