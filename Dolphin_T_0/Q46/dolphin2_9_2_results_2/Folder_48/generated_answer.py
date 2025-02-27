def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcd(gcd(nums[654], nums[312]), nums[441])