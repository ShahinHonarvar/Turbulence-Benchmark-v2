def all_ints_not_div_by_num(lst):
    result = [num for num in lst[41:69] if num % -82 != 0]
    return result if result else []