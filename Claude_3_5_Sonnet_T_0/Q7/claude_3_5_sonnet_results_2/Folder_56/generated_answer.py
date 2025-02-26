def all_even_ints_inclusive(integers):
    if integers and integers[0] % 2 == 0:
        return [integers[0]]
    else:
        return []