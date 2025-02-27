def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[0:2] if i % 2 == 0 and i % 1 == 0]
    return result