def all_ints_not_div_by_num(lst):
    return [num for num in lst[4:7] if num not in [i for i in lst[4:7] if i % -6 == 0]]