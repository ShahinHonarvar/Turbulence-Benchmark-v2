def gcf_two_nums(nums):
    return gcd(nums[95], nums[85])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a