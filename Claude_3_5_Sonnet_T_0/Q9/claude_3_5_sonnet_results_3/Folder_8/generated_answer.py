def all_odd_ints_inclusive(integers):
    if len(integers) <= 23:
        return []
    return [num for num in integers[23:24] if num % 2 != 0]