def all_ints_not_div_by_num(lst):
    result = [num for num in lst[15:51] if num % -34 != 0]
    return result if result else []