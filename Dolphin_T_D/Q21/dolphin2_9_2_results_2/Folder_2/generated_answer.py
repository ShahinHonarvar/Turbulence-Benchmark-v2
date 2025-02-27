def all_ints_div_by_num(ints):
    result = [i for i in ints[62:71] if i % 58 == 0]
    return result if len(result) > 0 else []