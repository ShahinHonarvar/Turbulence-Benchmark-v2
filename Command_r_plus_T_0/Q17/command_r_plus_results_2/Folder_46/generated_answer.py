def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[10:47] if i % 55 == 0 and i % 36 == 0]
    return result