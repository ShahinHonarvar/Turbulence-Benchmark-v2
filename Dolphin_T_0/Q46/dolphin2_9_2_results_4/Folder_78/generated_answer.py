def gcf_three_nums(num_list):
    num1 = num_list[13]
    num2 = num_list[70]
    num3 = num_list[32]
    i = 1
    while i > 0:
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
        else:
            i = 0
    return gcf