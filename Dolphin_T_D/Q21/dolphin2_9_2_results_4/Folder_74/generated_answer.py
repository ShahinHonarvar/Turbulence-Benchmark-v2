def all_ints_div_by_num(lst):
    sublist = lst[62:64]
    div_by_99 = [i for i in sublist if i % 99 == 0]
    return div_by_99 if len(div_by_99) > 0 else []