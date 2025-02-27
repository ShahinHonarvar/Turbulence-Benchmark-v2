def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[90:98] if i % 13 == 0 and i % 35 == 0]
    return result