def all_ints_div_by_both_two_nums(lst):
    if not lst[86:89]:
        return []
    return [i for i in lst[86:89] if not i % (61 * 79)]