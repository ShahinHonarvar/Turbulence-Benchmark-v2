def all_ints_div_by_num(lst):
    if len(lst) < 72:
        return []
    return [i for i in lst[70:72] if i % 85 == 0]