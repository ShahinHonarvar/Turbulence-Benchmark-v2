def gcf_two_nums(num_list):
    num1 = num_list[47]
    num2 = num_list[10]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1