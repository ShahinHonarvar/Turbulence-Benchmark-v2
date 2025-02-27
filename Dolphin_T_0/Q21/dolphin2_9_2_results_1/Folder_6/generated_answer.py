def all_ints_div_by_num(l):
    div_by_46 = [i for i in l[13:64] if i % 46 == 0]
    return div_by_46 if len(div_by_46) > 0 else []