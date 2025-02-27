def all_odd_ints_inclusive(integers):
    if len(integers) < 31:
        return []
    return [x for x in integers[30:49] if x % 2 != 0]