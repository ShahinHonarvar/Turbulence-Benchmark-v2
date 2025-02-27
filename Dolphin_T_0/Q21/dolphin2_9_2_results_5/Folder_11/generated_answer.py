def all_ints_div_by_num(lst_ints):
    div_by_neg61 = [i for i in lst_ints[22:64] if i % -61 == 0]
    if len(div_by_neg61) == 0:
        return []
    else:
        return div_by_neg61