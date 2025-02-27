def gcf_two_nums(nums):
    return gcd(nums[48], nums[76])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a