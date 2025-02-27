def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a

def gcf_three_nums(list_nums):
    return gcd(gcd(list_nums[17], list_nums[88]), list_nums[35])