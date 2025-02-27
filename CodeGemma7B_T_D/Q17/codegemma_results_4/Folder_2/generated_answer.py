def all_ints_div_by_both_two_nums(list):
    return list[73:87] if any((i % 54 == 0 and i % 82 == 0 for i in list[73:87])) else []