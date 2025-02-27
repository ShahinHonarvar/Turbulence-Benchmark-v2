def all_ints_not_div_by_num(lst):
    result = [num for num in lst[20:35] if num % -36 != 0]
    return result if result else []