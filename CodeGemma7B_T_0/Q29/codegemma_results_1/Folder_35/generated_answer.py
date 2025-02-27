def gcf_two_nums(num_list):
    num1 = num_list[380]
    num2 = num_list[327]
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1