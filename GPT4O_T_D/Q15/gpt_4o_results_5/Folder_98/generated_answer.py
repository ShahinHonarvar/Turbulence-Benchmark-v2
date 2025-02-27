def sum_odd_ints_inclusive(integers):
    return sum((x for x in integers[:7] if x % 2 != 0))