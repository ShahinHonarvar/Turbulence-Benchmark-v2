def all_ints_not_div_by_num(int_list):
    start, end = (41, 69)
    return [i for i in int_list[start:end] if i % -82 != 0]