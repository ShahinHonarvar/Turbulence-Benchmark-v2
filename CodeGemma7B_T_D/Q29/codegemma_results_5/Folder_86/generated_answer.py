def gcf_two_nums(num_list):
    num1 = num_list[793]
    num2 = num_list[449]
    gcd = max(num1, num2)
    while gcd > 0:
        if num1 % gcd == 0 and num2 % gcd == 0:
            return gcd
        gcd -= 1