def sum_odd_ints_inclusive(lst):
    try:
        return sum((val for val in lst[32:36] if val % 2 == 1))
    except IndexError:
        return 0