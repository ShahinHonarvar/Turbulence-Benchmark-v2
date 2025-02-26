def all_odd_ints_inclusive(integers):
    if len(integers) > 60:
        return [integers[60]] if integers[60] % 2 != 0 else []
    else:
        return []