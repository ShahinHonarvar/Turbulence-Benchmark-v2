def sum_even_ints_inclusive(lst):
    try:
        total = sum([x for x in lst[42:52] if x % 2 == 0])
    except IndexError:
        return 0
    return total