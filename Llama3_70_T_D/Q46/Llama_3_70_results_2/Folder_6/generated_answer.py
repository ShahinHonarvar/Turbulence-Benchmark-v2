def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcd(gcd(nums[93], nums[94]), nums[57])