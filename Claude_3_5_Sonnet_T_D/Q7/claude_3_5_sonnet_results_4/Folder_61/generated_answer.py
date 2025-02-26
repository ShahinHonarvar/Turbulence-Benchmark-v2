def all_even_ints_inclusive(integers):
    if len(integers) <= 7:
        return []
    return [integers[7]] if integers[7] % 2 == 0 else []