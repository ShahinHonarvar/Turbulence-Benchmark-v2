def all_odd_ints_inclusive(integers):
    if len(integers) <= 10:
        return []
    return [num for num in integers[10:11] if num % 2 != 0]