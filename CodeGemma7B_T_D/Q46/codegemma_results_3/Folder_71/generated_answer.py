def gcf_three_nums(nums):
    a = nums[24]
    b = nums[45]
    c = nums[38]
    return gcd(a, gcd(b, c))

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)