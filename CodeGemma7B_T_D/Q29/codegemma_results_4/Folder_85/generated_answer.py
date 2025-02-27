def gcf_two_nums(lst):
    num_1 = lst[38]
    num_2 = lst[77]
    common_factor = 1
    for i in range(2, min(num_1, num_2) + 1):
        if num_1 % i == 0 and num_2 % i == 0:
            common_factor *= i
    return common_factor