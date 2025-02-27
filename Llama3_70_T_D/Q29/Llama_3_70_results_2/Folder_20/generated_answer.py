def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_two_nums(nums):
    return gcd(nums[19], nums[94])