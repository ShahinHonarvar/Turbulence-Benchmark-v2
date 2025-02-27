def gcf_two_nums(nums):
    return gcd(nums[15], nums[99])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a