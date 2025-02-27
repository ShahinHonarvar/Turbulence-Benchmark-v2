def all_ints_not_div_by_num(ints):
    result = [i for i in ints[18:60] if i % 86 != 0]
    return result if result else []