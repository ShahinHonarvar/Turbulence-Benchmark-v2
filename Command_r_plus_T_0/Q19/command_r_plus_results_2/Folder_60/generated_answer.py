def all_ints_not_div_by_num(lst):
    return [num for i, num in enumerate(lst) if num % -99 != 0 and 63 <= i < 73]