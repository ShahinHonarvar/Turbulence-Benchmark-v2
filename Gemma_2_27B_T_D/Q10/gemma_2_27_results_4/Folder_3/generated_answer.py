def all_odd_ints_exclusive(ints):
    return [num for i, num in enumerate(ints) if i in range(78, 93) and num % 2 != 0]