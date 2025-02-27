def gcf_two_nums(nums):
    return gcd(nums[56], nums[92])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a