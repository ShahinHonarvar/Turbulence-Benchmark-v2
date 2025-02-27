def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def gcf_three_nums(nums):
    return gcd(gcd(nums[90], nums[84]), nums[47])