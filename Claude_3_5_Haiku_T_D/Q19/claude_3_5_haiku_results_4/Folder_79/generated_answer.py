def all_ints_not_div_by_num(lst):
    if len(lst) <= 9:
        return []
    result = [num for num in lst[9:] if num % -3 != 0]
    return result