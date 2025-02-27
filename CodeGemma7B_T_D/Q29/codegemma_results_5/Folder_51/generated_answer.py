def gcf_two_nums(int_list):
    num1 = int_list[46]
    num2 = int_list[84]
    gcd = num1
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return gcd