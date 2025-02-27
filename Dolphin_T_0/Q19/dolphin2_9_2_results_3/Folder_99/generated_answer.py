def all_ints_not_div_by_num(lst):
    result = [num for num in lst[387:516] if num % 310 != 0]
    return result if result else []