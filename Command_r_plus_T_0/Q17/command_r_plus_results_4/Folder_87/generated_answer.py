def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[18:53] if i % 15 == 0 and i % 57 == 0]
    return result