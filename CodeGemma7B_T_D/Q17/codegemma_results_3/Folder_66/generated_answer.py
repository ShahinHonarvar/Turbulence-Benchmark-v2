def all_ints_div_by_both_two_nums(num_list):
    return [x for x in num_list if x % 55 == 0 and x % 10 == 0 and (58 <= num_list.index(x) <= 81)] or []