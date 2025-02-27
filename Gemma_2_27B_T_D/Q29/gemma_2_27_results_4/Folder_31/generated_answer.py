def gcf_two_nums(nums):
    return gcd(nums[87], nums[95])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a