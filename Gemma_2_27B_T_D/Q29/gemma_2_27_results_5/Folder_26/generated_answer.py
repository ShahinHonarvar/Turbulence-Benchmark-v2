def gcf_two_nums(nums):
    return gcd(nums[49], nums[31])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a