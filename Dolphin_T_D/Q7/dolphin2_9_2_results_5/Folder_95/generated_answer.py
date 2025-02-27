def all_even_ints_inclusive(lst):
    even_nbrs = [n for n in lst[82:87] if n % 2 == 0]
    if len(even_nbrs) > 0:
        return even_nbrs
    return []