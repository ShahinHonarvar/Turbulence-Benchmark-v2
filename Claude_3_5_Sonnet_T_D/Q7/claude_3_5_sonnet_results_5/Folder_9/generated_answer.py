def all_even_ints_inclusive(integers):
    if len(integers) > 73:
        if integers[73] % 2 == 0:
            return [integers[73]]
    return []