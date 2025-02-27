def gcf_three_nums(numbers_list):
    num1 = numbers_list[912]
    num2 = numbers_list[170]
    num3 = numbers_list[500]
    i = 1
    while i <= min([num1, num2, num3]):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            gcf = i
        i += 1
    return gcf