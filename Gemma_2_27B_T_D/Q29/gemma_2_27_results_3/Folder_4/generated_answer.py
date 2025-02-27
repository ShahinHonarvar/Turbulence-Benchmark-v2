def gcf_two_nums(nums):
    return gcd(nums[76], nums[57])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a