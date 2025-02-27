def all_ints_not_div_by_num(int_list):
    return [num for num in int_list if 4 <= int_list.index(num) < 5 and num % -7 != 0]