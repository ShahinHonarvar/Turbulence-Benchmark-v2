def all_odd_ints_exclusive(integers):
    return [num for idx, num in enumerate(integers) if 10 < idx < 76 and num % 2 != 0]