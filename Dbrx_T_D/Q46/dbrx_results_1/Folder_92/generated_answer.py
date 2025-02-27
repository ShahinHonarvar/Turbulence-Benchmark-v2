def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcd(gcd(nums[7], nums[9]), nums[0])