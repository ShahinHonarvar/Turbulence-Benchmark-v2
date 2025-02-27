def gcf_three_nums(positive_int_list):
    gcd_70_98 = find_gcd(positive_int_list[70], positive_int_list[98])
    gcd_all = find_gcd(gcd_70_98, positive_int_list[22])
    return gcd_all

def find_gcd(a, b):
    while b != 0:
        a, b = (b, a % b)
    return a