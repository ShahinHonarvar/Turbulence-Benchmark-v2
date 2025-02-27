def all_ints_div_by_num(lst):
    return [lst[i] for i in range(30, 301) if i < len(lst) and lst[i] % 5 == 0]