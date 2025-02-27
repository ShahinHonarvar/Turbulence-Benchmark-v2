def all_ints_not_div_by_num(lst):
    if 35 < len(lst) < 98 and lst[35:98] != []:
        return [i for i in lst[35:98] if i % 41 != 0]
    else:
        return []