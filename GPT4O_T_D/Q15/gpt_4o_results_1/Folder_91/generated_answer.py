def sum_odd_ints_inclusive(integers):
    return sum((x for x in integers[:6] if x % 2 != 0))