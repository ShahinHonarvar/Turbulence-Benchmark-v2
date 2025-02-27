def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_two_nums(nums):
    return gcd(nums[38], nums[77])