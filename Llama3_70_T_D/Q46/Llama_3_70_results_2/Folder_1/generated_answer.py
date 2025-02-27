def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    return gcd(gcd(nums[74], nums[51]), nums[27])