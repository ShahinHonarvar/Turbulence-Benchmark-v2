def gcf_two_nums(num_list):
    num1 = num_list[184]
    num2 = num_list[307]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1