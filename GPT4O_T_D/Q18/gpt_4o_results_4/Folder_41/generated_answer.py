def sum_ints_div_by_either_nums(int_list):
    if not int_list:
        return 0
    max_index = min(9, len(int_list) - 1)
    return sum((x for x in int_list[:max_index + 1] if x % 6 == 0 or x % -3 == 0))