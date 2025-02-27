def all_ints_div_by_num(ints):
    result = [int for i, int in enumerate(ints[10:11]) if int % 1 == 0]
    return result if result else []