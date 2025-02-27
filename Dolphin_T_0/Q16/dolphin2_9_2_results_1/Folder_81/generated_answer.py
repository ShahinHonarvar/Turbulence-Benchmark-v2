def sum_even_ints_inclusive(lst):
    result = 0
    for i, val in enumerate(lst[10:101], start=10):
        if val % 2 == 0:
            result += val
    return result