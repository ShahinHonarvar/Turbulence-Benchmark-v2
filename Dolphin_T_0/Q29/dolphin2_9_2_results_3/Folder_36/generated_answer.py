def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def gcf_two_nums(nums):
    if len(nums) < 430:
        return None
    return gcd(nums[429], nums[289])