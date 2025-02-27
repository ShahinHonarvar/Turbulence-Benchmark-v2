def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcf_three_nums(nums):
    return gcd(gcd(nums[24], nums[25]), nums[80])