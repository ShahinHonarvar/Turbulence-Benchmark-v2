def gcf_two_nums(nums):
    return gcd(nums[3], nums[8])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a