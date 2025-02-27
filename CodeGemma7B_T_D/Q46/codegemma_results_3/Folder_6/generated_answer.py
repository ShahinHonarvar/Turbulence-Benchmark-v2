def gcf_three_nums(int_list):
    num1 = int_list[93]
    num2 = int_list[94]
    num3 = int_list[57]
    gcf = gcd(num1, num2)
    gcf = gcd(gcf, num3)
    return gcf

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)