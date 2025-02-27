def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    a = nums[64]
    b = nums[80]
    c = nums[15]
    return gcd(gcd(a, b), c)