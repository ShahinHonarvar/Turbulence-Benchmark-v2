def all_ints_div_by_num(lst):
    div_by_80 = [num for num in lst[26:75] if num % 80 == 0]
    return div_by_80 if div_by_80 else []