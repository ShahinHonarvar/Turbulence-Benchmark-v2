def all_ints_not_div_by_num(lst):
    result = [num for num in lst[70:200] if num % -300 != 0]
    return result