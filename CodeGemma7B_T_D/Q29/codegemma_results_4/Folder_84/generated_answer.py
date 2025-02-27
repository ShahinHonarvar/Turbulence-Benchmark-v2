def gcf_two_nums(num_list):
    num1 = num_list[360]
    num2 = num_list[722]
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        elif num1 < num2:
            num2 -= num1
    return num1