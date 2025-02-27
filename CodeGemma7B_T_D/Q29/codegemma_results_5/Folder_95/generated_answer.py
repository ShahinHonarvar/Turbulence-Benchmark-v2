def gcf_two_nums(int_list):
    num1 = int_list[43]
    num2 = int_list[99]
    while num2:
        num1, num2 = (num2, num1 % num2)
    return num1