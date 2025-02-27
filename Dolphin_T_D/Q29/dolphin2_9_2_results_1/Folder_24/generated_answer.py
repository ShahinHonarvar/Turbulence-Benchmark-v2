def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_two_nums(nums):
    a = nums[84]
    b = nums[21]
    return gcd(a, b)