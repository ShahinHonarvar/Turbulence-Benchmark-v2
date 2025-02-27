def all_ints_div_by_num(lst):
    try:
        return [num for num in lst[34:56] if num % -83 == 0]
    except Exception:
        return []