def all_ints_div_by_num(int_list):
    return [num for num in int_list if num % 2 == 0 and num in range(int_list[0], int_list[1] + 1)]