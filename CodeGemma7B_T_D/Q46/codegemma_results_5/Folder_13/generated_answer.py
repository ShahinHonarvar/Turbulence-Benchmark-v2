def gcf_three_nums(nums):
    a = nums[991]
    b = nums[244]
    c = nums[974]
    gcd = find_gcd(a, b)
    gcd = find_gcd(gcd, c)
    return gcd

def find_gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a