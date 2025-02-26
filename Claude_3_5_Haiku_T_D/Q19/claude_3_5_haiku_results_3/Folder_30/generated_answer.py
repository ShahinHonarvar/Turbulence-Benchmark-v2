def all_ints_not_div_by_num(lst):
    if len(lst) <= 35:
        return []
    result = [num for num in lst[21:35] if num % -36 != 0]
    return result