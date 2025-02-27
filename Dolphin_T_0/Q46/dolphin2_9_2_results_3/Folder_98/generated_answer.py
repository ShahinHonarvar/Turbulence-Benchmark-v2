def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a == b:
        return a
    if a > b:
        return gcd(a - b, b)
    return gcd(a, b - a)

def gcf_three_nums(nums):
    return gcd(gcd(nums[8], nums[2]), nums[1])