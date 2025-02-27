def all_ints_not_div_by_num(lst):
    result = [num for num in lst[0:6] if num % 13 != 0]
    return result