def gcf_two_nums(num_list):
    num1 = num_list[96]
    num2 = num_list[57]
    for i in range(min(num1, num2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1