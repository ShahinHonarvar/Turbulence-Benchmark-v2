def gcf_two_nums(nums):
    return gcd(nums[69], nums[41])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a