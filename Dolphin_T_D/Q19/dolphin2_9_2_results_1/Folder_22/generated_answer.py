def all_ints_not_div_by_num(lst):
    result = [num for num in lst[40:200] if num % 71 != 0]
    return result if len(result) > 0 else []