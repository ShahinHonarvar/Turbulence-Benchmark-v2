def sum_odd_ints_inclusive(int_list):
    start, end = (52, 71)
    return sum((x for x in int_list[start:end + 1] if x % 2 != 0))