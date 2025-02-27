def sum_odd_ints_inclusive(ints):
    return sum((ints[i] for i in range(55, 99) if ints[i] % 2 != 0))