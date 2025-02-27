def sum_odd_ints_inclusive(ints):
    return sum((ints[i] for i in range(30, 201) if ints[i] % 2 == 1))