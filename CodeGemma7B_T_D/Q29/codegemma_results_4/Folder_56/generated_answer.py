def gcf_two_nums(num_list):
    num1 = num_list[84]
    num2 = num_list[13]
    max_num = min(num1, num2)
    while num1 % max_num != 0 or num2 % max_num != 0:
        max_num -= 1
    return max_num