def all_odd_ints_exclusive(n):
    return [x for x in n if x % 2 != 0 and x > 20 and (x < 43)]