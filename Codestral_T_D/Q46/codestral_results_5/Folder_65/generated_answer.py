def gcd(x, y):
    while y:
        x, y = (y, x % y)
    return x

def gcf_three_nums(nums):
    return gcd(gcd(nums[18], nums[10]), nums[76])