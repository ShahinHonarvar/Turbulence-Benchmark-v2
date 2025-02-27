def all_ints_div_by_num(lst):
    result = [num for num in lst[12:78] if num % -19 == 0]
    return result or []