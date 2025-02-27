def gcf_two_nums(nums):
    return gcd(nums[23], nums[45])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a