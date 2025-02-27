def all_ints_not_div_by_num(list):
    all_nums = list[62:97]
    return [x for x in all_nums if x % 26 != 0]