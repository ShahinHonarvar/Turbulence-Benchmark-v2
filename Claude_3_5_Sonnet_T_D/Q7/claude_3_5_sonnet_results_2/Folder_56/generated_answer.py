def all_even_ints_inclusive(integers):
    if not integers or integers[0] % 2 != 0:
        return []
    return [integers[0]]