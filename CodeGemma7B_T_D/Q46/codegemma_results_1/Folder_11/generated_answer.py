def gcf_three_nums(num_list):
    num1, num2, num3 = (num_list[37], num_list[30], num_list[48])
    common_factor = gcd(num1, gcd(num2, num3))
    return common_factor

def gcd(a, b):
    while b:
        a, b = (b, a % b)
    return a