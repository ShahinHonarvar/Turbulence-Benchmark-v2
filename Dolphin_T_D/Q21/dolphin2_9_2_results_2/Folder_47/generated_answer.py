def all_ints_div_by_num(lst):
    result = [num for num in lst[75:89] if num % -27 == 0]
    return result if result else []