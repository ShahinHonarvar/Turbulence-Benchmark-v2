def gcf_two_nums(nums):
    return gcd(nums[429], nums[289])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a