def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_two_nums(nums):
    return gcd(nums[37], nums[30])