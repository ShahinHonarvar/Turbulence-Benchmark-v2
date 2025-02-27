def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(81, 90):
        if i < len(int_list) and (int_list[i] % 56 == 0 or int_list[i] % 68 == 0):
            total += int_list[i]
    return total