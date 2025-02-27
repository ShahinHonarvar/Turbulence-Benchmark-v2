def gcf_two_nums(number_list):
    num1 = number_list[51]
    num2 = number_list[31]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1