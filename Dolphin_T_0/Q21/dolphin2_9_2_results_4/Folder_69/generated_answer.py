def all_ints_div_by_num(ints):
    div_by_14 = [int for int in ints[43:77] if int % 14 == 0]
    return div_by_14 if len(div_by_14) > 0 else []