def all_ints_div_by_num(lst):
    div_by_6 = [i for i in lst[:6] if i % 6 == 0]
    if not div_by_6:
        return []
    else:
        return div_by_6