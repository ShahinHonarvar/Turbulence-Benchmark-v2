def all_ints_not_div_by_num(lst):
    if len(lst) <= 21:
        return []
    result = [num for num in lst[16:20] if num % 93 != 0]
    return result