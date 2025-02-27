def all_odd_ints_exclusive(integers):
    return [num for i, num in enumerate(integers) if 18 < i < 60 and num % 2 != 0]