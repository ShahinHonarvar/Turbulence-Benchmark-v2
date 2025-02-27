def sum_odd_ints_inclusive(values):
    return sum((v % 2 for v in values[0:10] if v % 2 != 0)) or 0