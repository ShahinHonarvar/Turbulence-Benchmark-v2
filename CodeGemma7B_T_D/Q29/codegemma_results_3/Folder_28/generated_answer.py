def gcf_two_nums(nums):
    a, b = (nums[48], nums[76])
    return gcd(a, b)

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a