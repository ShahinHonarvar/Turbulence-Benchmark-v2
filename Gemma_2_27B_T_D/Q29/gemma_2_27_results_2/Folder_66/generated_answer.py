def gcf_two_nums(nums):
    return gcd(nums[86], nums[89])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a