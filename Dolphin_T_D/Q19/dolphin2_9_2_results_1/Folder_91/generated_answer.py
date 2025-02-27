def all_ints_not_div_by_num(lst):
    result = [num for num in lst[5:] if num % 8 != 0]
    return result