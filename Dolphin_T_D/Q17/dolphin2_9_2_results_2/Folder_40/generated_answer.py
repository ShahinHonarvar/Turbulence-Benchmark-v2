def all_ints_div_by_both_two_nums(l):
    result = [i for i in l[0:2] if i % 2 == 0 and i % 1 == 0]
    return result if len(result) > 0 else []