def gcf_two_nums(nums):
    return gcd(nums[47], nums[97])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a