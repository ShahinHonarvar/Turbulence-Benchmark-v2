def gcf_two_nums(nums):
    return gcd(nums[38], nums[77])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a