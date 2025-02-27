def all_odd_ints_inclusive(lst):
    return [num for i, num in enumerate(lst) if i in range(15, 40) and num % 2 != 0]