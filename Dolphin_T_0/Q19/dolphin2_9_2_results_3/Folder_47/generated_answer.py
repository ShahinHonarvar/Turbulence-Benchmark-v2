def all_ints_not_div_by_num(lst):
    result = [num for num in lst[25:76] if num % -53 != 0]
    return result