def gcf_two_nums(num_list):
    num1 = num_list[95]
    num2 = num_list[85]
    for i in range(min(num1, num2), 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1