def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcf_three_nums(numb_list):
    return gcd(gcd(numb_list[90], numb_list[41]), numb_list[95])