def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_three_nums(nums):
    return gcd(gcd(nums[90], nums[84]), nums[47])