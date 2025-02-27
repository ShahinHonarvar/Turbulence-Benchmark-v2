def gcf_two_nums(num_list):
    num1 = num_list[46]
    num2 = num_list[84]
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1