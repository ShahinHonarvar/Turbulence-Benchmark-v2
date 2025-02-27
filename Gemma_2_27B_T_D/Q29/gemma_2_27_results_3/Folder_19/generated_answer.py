def gcf_two_nums(nums):
    return gcd(nums[66], nums[90])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a