def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def gcf_two_nums(num_list):
    return gcd(num_list[91], num_list[45])