def sum_odd_ints_inclusive(lst):
    return sum((val for i, val in enumerate(lst[17:79], start=17) if i % 2 != 0))