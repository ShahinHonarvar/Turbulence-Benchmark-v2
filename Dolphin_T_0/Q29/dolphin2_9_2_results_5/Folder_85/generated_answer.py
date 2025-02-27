def gcf_two_nums(num_list):
    num1 = num_list[38]
    num2 = num_list[77]
    i = min(num1, num2)
    while i > 1:
        if num1 % i == 0 and num2 % i == 0:
            return i
        i -= 1
    return 1