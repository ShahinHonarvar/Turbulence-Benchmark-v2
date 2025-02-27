def all_ints_div_by_num(lst):
    return [i for i in lst if not i % 7 and i in range(0, len(lst), +1)]