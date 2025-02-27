def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[30:201] if i % -115 == 0 and i % 115 == 0]
    return result