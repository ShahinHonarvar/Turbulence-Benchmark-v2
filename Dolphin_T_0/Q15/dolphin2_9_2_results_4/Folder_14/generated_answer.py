def sum_odd_ints_inclusive(ints):
    try:
        return sum((x for x in ints[4:8] if x % 2 == 1))
    except IndexError:
        return 0