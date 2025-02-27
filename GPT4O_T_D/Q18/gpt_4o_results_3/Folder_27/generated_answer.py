def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 36:
        return 0
    return sum((x for x in int_list[20:36] if x % -36 == 0 or x % -89 == 0))