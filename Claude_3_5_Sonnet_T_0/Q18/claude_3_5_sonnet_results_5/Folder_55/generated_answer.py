def sum_ints_div_by_either_nums(int_list):
    total = 0
    for i in range(min(10, len(int_list))):
        if int_list[i] % 10 == 0 or int_list[i] % 100 == 0:
            total += int_list[i]
    return total