def all_even_ints_inclusive(lst):
    return [even for even in lst if even % 2 == 0 and 55 <= lst.index(even) <= 98]