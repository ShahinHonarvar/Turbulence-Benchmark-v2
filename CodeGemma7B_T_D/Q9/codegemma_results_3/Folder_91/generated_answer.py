def all_odd_ints_inclusive(xs):
    return [x for x in xs if x % 2 != 0 and x in range(6)] or []