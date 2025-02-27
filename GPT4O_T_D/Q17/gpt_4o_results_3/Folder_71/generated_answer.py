def all_ints_div_by_both_two_nums(int_list):
    if len(int_list) < 100:
        return []
    return [x for x in int_list[68:100] if x % 37 == 0 and x % 26 == 0]