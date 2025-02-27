def all_ints_not_div_by_num(lst):
    return [lst[i] for i in range(20, len(lst)) if i < 50 and lst[i] % -36 != 0]