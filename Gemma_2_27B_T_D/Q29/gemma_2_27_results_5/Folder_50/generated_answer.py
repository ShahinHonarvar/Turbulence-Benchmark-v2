def gcf_two_nums(nums):
    return gcd(nums[90], nums[54])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a