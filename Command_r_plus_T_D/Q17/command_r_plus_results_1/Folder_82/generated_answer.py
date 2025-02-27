def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[20:201] if i % -20 == 0 and i % -200 == 0]
    return result