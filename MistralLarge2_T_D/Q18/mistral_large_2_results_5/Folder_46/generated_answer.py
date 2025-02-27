def sum_ints_div_by_either_nums(ints_list):
    return sum((x for x in ints_list[11:47] if x % 55 == 0 or x % 36 == 0))