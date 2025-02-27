def all_ints_not_div_by_num(lst, num):
    if len(lst) < 98:
        return []
    return [num for num in lst[35:98] if num % 41 != 0]