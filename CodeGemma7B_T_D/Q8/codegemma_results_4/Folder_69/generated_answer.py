from itertools import islice, filterfalse

def all_even_ints_exclusive(lst):
    return list(filterfalse(lambda e: e % 2, islice(lst, 68, 99)))