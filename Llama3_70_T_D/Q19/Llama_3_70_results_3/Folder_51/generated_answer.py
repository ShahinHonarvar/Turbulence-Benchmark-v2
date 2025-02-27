def all_ints_not_div_by_num(lst):
    return [lst[i] for i in range(1, 7) if i < len(lst) and lst[i] % 2 != 0]