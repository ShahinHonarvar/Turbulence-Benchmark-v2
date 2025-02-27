def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[50:201] if i % -34 == 0 and i % 64 == 0]
    return result