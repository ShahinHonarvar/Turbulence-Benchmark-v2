def all_ints_not_div_by_num(lst):
    result = [num for num in lst[30:200] if num % -115 != 0]
    return result if result else []