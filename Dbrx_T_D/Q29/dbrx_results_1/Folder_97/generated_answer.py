def gcf_two_nums(int_list):
    num1 = int_list[180]
    num2 = int_list[312]
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i