def gcf_three_nums(num_list):
    num1 = num_list[7]
    num2 = num_list[9]
    num3 = num_list[0]
    gcd = num1
    if num2 > gcd:
        gcd = num2
    if num3 > gcd:
        gcd = num3
    return gcd