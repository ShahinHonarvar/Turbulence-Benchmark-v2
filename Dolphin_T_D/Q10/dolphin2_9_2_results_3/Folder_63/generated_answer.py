def all_odd_ints_exclusive(lst):
    return [num for i, num in enumerate(lst) if i in range(38, 52) and num % 2 == 1]