def all_odd_ints_inclusive(integers):
    if len(integers) < 5:
        return []
    return [num for num in integers[4:5] if num % 2 != 0]