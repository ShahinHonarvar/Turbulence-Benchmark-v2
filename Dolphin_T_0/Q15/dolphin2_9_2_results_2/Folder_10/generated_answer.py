def sum_odd_ints_inclusive(ints):
    return sum((int for i, int in enumerate(ints[25:60]) if i % 2 != 0))