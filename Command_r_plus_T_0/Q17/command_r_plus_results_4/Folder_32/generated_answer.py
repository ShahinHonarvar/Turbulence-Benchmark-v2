def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[24:96] if i % 51 == 0 and i % 77 == 0]
    return result