def gcf_three_nums(num_list):
    num1, num2, num3 = (num_list[96], num_list[57], num_list[85])
    while num2 != 0:
        num1, num2 = (num2, num1 % num2)
    return num1