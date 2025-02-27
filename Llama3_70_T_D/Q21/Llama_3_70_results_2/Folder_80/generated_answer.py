def all_ints_div_by_num(lst):
    return [lst[i] for i in range(27, 87) if i < len(lst) and lst[i] % 29 == 0]