def all_ints_not_div_by_num(lst):
    result = [num for num in lst[24:32] if num % 35 != 0]
    return result if result else []