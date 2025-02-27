def all_ints_not_div_by_num(lst):
    return [x for x in lst[1:-1] if lst[0] != 0 and lst[1] != 0 and (x % lst[0] != 0) and (x % lst[1] != 0)]