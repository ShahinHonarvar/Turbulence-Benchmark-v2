def gcf_two_nums(nums):
    return gcd(nums[42], nums[25])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a