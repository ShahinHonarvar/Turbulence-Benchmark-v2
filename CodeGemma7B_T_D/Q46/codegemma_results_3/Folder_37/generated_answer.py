def gcf_three_nums(num_list):
    num1 = num_list[41]
    num2 = num_list[69]
    num3 = num_list[28]
    '\n                Traditional GCD algorithm\n                '
    while num1 != 0 and num2 != 0:
        if num1 < num2:
            num1, num2 = (num2, num2 % num1)
        else:
            num2, num3 = (num3, num3 % num2)
    gcd = num1
    return gcd