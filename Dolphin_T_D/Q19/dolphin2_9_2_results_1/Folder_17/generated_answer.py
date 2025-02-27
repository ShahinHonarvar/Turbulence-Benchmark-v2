def all_ints_not_div_by_num(lst):
    result = [num for num in lst[39:57] if num % 84 != 0]
    return result if result else []