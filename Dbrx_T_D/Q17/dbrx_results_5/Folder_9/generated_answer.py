def all_ints_div_by_both_two_nums(lst):
    if len(lst) < 200 or not isinstance(lst[199], int) or (not isinstance(lst[69], int)):
        return []
    return [i for i in lst[70:201] if i % 3 == 0 and i % -300 == 0]