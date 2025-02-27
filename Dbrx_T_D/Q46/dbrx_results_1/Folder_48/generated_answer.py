def gcf_three_nums(nums):
    gcd1 = gcd(nums[654], nums[312])
    gcd2 = gcd(gcd1, nums[441])
    return gcd2

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)