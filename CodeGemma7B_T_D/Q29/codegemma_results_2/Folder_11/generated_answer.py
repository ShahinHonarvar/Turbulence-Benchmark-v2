def gcf_two_nums(integer_list):
    num1 = integer_list[64]
    num2 = integer_list[80]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1