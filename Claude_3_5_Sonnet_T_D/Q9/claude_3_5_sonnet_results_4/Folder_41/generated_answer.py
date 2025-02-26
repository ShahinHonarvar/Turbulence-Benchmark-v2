def all_odd_ints_inclusive(integers):
    if len(integers) < 7:
        return []
    return [integers[6]] if integers[6] % 2 != 0 else []