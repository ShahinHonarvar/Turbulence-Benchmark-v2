def all_ints_div_by_num(lst):
    result = [n for i, n in enumerate(lst[45:81]) if n % 39 == 0]
    return result