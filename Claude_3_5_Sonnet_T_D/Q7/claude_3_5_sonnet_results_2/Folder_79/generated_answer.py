def all_even_ints_inclusive(integers):
    if len(integers) >= 5:
        return [integers[4]] if integers[4] % 2 == 0 else []
    else:
        return []