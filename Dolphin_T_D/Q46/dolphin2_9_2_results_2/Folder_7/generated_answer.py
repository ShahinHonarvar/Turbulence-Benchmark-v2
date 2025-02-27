def gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a

def gcf_three_nums(nums_list):
    return gcd(nums_list[477], gcd(nums_list[696], nums_list[663]))