def sum_odd_ints_inclusive(lst):
    if len(lst) < 5:
        return sum(filter(lambda x: x % 2 != 0, lst[:5]))
    else:
        return sum(filter(lambda x: x % 2 != 0, lst[:5]))