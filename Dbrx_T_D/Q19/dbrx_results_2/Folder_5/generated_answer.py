def all_ints_not_div_by_num(int_list):
    start, end = (1, 2)
    return [num for num in int_list[start:end] if num % 8 != 0]