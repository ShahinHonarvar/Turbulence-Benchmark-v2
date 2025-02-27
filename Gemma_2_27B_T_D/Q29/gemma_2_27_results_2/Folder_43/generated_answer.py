def gcf_two_nums(nums):
    return gcd(nums[59], nums[93])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a