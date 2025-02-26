def all_ints_div_by_num(lst):
    if len(lst) <= 23:
        return []
    target_list = lst[23:24]
    return [num for num in target_list if num % -57 == 0]