def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if i in range(209, 557) and num % 2 != 0]