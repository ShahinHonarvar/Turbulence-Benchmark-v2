def sum_odd_ints_inclusive(integers):
    return sum((i for i in integers[30:201] if i % 2 != 0))