def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcd(nums[0], gcd(nums[4], nums[8]))