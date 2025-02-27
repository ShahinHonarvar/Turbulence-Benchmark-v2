def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_three_nums(nums_list):
    return gcd(nums_list[10], gcd(nums_list[55], nums_list[36]))