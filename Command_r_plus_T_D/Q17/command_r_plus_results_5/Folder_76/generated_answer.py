def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[249:630] if i % 850 == 0 and i % 587 == 0]
    return result