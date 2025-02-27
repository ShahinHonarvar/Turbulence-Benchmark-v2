def gcf_two_nums(nums):
    return gcd(nums[166], nums[106])

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a