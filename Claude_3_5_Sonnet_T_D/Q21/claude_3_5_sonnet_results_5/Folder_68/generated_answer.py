def all_ints_div_by_num(integers):
    if not integers:
        return []
    return [integers[0]] if integers[0] % 8 == 0 else []