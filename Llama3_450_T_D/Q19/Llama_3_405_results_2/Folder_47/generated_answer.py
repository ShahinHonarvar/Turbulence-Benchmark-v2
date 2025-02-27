def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst[25:76]) if num % -53 != 0]