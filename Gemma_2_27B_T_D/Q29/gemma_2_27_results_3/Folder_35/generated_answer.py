def gcf_two_nums(nums):
    return gcd(nums[380], nums[327])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a