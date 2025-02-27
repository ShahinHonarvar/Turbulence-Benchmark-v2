def gcf_three_nums(my_list):
    num1 = my_list[20]
    num2 = my_list[17]
    num3 = my_list[28]
    gcf = 1
    for i in range(1, min(num1, num2, num3) + 1):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
    return gcf