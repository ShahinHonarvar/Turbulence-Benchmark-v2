def all_odd_ints_inclusive(integers):
    if len(integers) <= 60:
        return []
    return [num for num in integers[60:61] if num % 2 != 0]