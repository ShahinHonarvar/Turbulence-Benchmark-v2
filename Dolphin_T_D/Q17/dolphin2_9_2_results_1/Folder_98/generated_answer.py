def all_ints_div_by_both_two_nums(integers_list):
    return [x for x in integers_list[0:6] if x % -1 == 0 and x % 13 == 0]