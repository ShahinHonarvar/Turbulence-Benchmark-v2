def gcd(x, y):
    while y:
        x, y = (y, x % y)
    return x

def gcf_three_nums(nums):
    return gcd(nums[91], gcd(nums[45], nums[48]))