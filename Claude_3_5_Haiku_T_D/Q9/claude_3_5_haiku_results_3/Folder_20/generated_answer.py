def all_odd_ints_inclusive(integers):
    if len(integers) <= 66:
        return []
    return [num for num in integers[56:67] if num % 2 != 0]