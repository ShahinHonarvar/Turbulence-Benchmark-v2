def gcf_two_nums(nums):
    return gcd(nums[534], nums[630])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a