def all_ints_div_by_num(lst):
    result = [num for num in lst[52:73] if num % -15 == 0]
    return result if result else []