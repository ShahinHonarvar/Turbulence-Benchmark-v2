def all_ints_div_by_num(lst):
    target_range = lst[26:87]
    div_by_29 = [num for num in target_range if num % 29 == 0]
    return div_by_29