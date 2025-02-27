def all_ints_not_div_by_num(lst):
    return [lst[i] for i in range(7, 10) if i < len(lst) and lst[i] % -9 != 0]