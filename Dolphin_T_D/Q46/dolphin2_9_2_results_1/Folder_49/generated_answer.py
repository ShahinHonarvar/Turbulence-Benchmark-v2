def gcf_three_nums(num_list):
    num1 = num_list[34]
    num2 = num_list[38]
    num3 = num_list[77]
    i = 1
    while i <= num1 and i <= num2 and (i <= num3):
        if num1 % i == 0 and num2 % i == 0 and (num3 % i == 0):
            result = i
        i += 1
    return result