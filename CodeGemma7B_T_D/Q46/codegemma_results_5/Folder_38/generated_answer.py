def gcf_three_nums(my_list):
    return gcd(my_list[14], gcd(my_list[21], my_list[17]))

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a