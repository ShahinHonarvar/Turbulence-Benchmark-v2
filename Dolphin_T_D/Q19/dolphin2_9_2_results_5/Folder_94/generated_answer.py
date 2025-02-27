def all_ints_not_div_by_num(lst):
    sublst = lst[24:45]
    result = [x for x in sublst if x % -72 != 0]
    return result