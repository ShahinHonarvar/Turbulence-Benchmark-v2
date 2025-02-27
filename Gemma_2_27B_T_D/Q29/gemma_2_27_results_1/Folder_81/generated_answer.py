def gcf_two_nums(nums):
    return gcd(nums[20], nums[83])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a