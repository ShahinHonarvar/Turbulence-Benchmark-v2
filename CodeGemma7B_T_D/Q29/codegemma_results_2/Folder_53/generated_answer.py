def gcf_two_nums(num_list):
    num1 = num_list[28]
    num2 = num_list[67]
    while num1 % num2 != 0:
        temp = num2
        num2 = num1 % num2
        num1 = temp
    return num2