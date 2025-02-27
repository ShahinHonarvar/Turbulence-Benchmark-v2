def all_ints_div_by_num(lst):
    return [lst[i] for i in range(2) if i < len(lst) and lst[i] % 2 == 0]