def sum_odd_ints_inclusive(lst):
    if len(lst) < 79:
        return 0
    return sum((i for i in lst[62:79] if i % 2 != 0))