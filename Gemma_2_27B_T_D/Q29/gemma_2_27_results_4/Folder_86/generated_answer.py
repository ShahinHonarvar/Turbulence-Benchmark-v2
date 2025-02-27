def gcf_two_nums(nums):
    return gcd(nums[793], nums[449])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a