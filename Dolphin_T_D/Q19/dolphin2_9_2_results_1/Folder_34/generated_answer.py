def all_ints_not_div_by_num(lst):
    result = [num for num in lst[60:200] if num % 9 != 0]
    return result