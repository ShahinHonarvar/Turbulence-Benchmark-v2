def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(31, 51):
        if i < len(int_list):
            if int_list[i] % 81 == 0 or int_list[i] % 64 == 0:
                total += int_list[i]
    return total