def gcf_two_nums(nums):
    return gcd(nums[85], nums[51])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a