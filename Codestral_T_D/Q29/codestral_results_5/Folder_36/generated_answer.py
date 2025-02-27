def gcf_two_nums(num_list):
    num1 = num_list[429]
    num2 = num_list[289]
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1