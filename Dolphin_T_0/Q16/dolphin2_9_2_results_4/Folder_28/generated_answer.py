def sum_even_ints_inclusive(lst):
    try:
        return sum(filter(lambda x: x % 2 == 0, lst[62:64]))
    except IndexError:
        return 0