def sum_odd_ints_inclusive(lst):
    return sum((i for idx, i in enumerate(lst) if 533 <= idx <= 605 and i % 2 != 0))