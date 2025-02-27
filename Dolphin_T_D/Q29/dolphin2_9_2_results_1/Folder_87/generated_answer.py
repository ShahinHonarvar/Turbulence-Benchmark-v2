def gcd(x, y):
    while y:
        x, y = (y, x % y)
    return x

def gcf_two_nums(nums):
    return gcd(nums[83], nums[14])