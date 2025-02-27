def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

def gcf_three_nums(nums):
    return gcd(nums[29], gcd(nums[74], nums[49]))