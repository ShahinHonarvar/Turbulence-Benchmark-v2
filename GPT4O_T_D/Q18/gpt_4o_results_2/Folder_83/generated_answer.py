def sum_ints_div_by_either_nums(int_list):
    if len(int_list) < 200:
        return 0
    return sum((x for x in int_list[90:201] if x % 31 == 0 or x % 13 == 0))