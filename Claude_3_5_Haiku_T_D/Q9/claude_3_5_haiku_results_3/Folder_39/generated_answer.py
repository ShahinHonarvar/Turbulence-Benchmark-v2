def all_odd_ints_inclusive(integers):
    if len(integers) < 31:
        return []
    return [num for num in integers[20:31] if num % 2 != 0]