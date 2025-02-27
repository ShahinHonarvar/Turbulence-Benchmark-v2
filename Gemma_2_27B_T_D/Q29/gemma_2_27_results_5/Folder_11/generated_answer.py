def gcf_two_nums(nums):
    return gcd(nums[64], nums[80])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a