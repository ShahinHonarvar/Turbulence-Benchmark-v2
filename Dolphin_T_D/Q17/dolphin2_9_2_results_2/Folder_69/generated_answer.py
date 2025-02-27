def all_ints_div_by_both_two_nums(lst):
    sublist = lst[61:89]
    result = [i for i in sublist if i % 31 == 0 and i % 11 == 0]
    return result