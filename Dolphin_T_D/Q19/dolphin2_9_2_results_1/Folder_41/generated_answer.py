def all_ints_not_div_by_num(lst):
    result = [num for i, num in enumerate(lst) if 0 < i < 9 and num % -3 != 0]
    if not result:
        return []
    return result