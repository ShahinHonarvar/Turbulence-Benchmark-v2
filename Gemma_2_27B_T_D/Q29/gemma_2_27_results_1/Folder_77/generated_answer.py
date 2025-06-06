def gcf_two_nums(nums):
    return gcd(nums[841], nums[804])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a