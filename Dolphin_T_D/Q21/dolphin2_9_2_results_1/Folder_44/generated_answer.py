def all_ints_div_by_num(lst):
    result = [num for num in lst[65:82] if num % 77 == 0]
    return result if result else []