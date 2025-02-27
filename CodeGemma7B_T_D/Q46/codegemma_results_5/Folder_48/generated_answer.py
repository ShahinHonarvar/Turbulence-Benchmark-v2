def gcf_three_nums(num_list):
    num1 = num_list[654]
    num2 = num_list[312]
    num3 = num_list[441]
    min_num = min(num1, num2, num3)
    for i in range(min_num, 0, -1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            return i