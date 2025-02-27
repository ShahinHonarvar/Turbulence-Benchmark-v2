def sum_odd_ints_inclusive(lst):
    return sum((val for i, val in enumerate(lst) if i in range(667, 775) and val % 2 == 1))