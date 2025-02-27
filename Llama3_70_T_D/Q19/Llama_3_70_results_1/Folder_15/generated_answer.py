def all_ints_not_div_by_num(lst):
    return [lst[i] for i in range(len(lst)) if 0 <= i < 3 and lst[i] % -2 != 0]