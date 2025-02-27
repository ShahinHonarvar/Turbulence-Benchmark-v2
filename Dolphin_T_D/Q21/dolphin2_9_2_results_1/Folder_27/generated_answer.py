def all_ints_div_by_num(lst):
    result = [n for n in lst[25:31] if n % -69 == 0]
    return result if len(result) > 0 else []