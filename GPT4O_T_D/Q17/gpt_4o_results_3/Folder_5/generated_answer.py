def all_ints_div_by_both_two_nums(int_list):
    if len(int_list) < 2:
        return []
    return [x for x in int_list[0:2] if x % 24 == 0]