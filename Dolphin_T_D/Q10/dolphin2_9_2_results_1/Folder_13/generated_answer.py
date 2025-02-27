def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i in range(73, 84) and num % 2 != 0]