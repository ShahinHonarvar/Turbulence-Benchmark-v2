def sum_odd_ints_inclusive(lst):
    if len(lst) < 37:
        return 'Input list must have at least 37 elements.'
    odd_ints = sum(filter(lambda x: x % 2 != 0, lst[33:37]))
    return odd_ints