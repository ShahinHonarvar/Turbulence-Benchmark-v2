def all_ints_div_by_both_two_nums(lst):
    result = [i for i in lst[40:201] if i % 21 == 0 and i % 71 == 0]
    return result if result else []