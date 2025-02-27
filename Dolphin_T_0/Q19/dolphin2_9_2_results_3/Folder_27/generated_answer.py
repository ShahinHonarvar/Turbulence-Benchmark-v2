def all_ints_not_div_by_num(lst):
    result = [num for num in lst[14:21] if num % -93 != 0]
    return result if result else []