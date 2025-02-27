def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_three_nums(num_list):
    return gcd(gcd(num_list[70], num_list[98]), num_list[22])