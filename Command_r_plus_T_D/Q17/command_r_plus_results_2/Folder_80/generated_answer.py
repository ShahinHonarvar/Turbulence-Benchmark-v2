def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[14:94] if i % 71 == 0 and i % 81 == 0]
    return result