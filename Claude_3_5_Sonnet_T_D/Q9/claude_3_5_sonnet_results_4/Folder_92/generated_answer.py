def all_odd_ints_inclusive(integers):
    if len(integers) < 2:
        return []
    return [num for num in integers[:2] if num % 2 != 0]