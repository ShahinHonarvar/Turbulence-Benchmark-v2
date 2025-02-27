def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def gcf_two_nums(nums):
    return gcd(nums[13], nums[66])