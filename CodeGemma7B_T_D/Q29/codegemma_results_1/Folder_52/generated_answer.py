def gcf_two_nums(num_list):
    num1 = num_list[90]
    num2 = num_list[41]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1