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

def gcf_two_nums(nums):
    if len(nums) < 76:
        return None
    return gcd(nums[48], nums[76])