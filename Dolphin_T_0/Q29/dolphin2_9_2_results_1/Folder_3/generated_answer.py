def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_two_nums(nums_list):
    return gcd(nums_list[47], nums_list[10])