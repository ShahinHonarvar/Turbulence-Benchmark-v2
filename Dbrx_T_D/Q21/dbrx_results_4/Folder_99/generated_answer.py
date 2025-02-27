def all_ints_div_by_num(integer_list):
    start, end = (161, 970)
    return [num for num in integer_list[start:end + 1] if num % 763 == 0]