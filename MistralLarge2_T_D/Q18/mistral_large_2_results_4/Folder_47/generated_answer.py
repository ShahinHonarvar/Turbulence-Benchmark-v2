def sum_ints_div_by_either_nums(int_list):
    return sum((x for i, x in enumerate(int_list[42:88]) if x % -90 == 0 or x % -74 == 0))