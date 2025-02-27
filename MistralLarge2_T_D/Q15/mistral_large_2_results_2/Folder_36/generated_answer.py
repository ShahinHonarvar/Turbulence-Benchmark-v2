def sum_odd_ints_inclusive(integers):
    return sum((x for x in integers[246:751] if x % 2 == 1))