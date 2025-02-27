def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums):
    a = nums[32]
    b = nums[54]
    c = nums[13]
    gcd_ac = gcd(a, c)
    return gcd(gcd_ac, b)