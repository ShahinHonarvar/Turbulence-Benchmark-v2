def gcf_three_nums(nums):
    a, b, c = (nums[40], nums[15], nums[99])
    return gcd(a, gcd(b, c))

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a