def all_ints_not_div_by_num(lst):
    result = [num for num in lst[1:6] if num % 2 != 0]
    return result if result else []