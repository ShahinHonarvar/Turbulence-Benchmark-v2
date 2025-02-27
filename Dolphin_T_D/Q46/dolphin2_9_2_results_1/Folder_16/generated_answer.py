def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_three_nums(nums):
    return gcd(nums[558], gcd(nums[110], nums[628]))