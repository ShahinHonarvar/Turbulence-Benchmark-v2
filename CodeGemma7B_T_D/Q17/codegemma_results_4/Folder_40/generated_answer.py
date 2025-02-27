def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst if i % 2 == 0 and i % 1 == 0 and (i >= lst[0]) and (i <= lst[1])]
    return result if result else []