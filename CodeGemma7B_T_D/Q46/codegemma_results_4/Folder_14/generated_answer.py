def gcf_three_nums(list_nums):
    a = list_nums[17]
    b = list_nums[88]
    c = list_nums[35]
    common_factor = gcd(a, b)
    common_factor = gcd(common_factor, c)
    return common_factor

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a