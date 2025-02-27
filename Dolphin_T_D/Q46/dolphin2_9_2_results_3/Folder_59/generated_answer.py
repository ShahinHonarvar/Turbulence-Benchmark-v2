def gcf_three_nums(num_list):
    num1 = num_list[7]
    num2 = num_list[6]
    num3 = num_list[8]
    i = 1
    gcf = 1
    while i <= min(num1, num2, num3):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
        i += 1
    return gcf