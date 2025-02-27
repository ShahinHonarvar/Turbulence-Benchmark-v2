def all_ints_not_div_by_num(lst):
    result = [num for num in lst[62:96] if num % 26 != 0]
    return result if result else []