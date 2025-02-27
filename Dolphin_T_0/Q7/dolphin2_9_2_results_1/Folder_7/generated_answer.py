def all_even_ints_inclusive(lst):
    result = [x for x in lst[661:925:2] if x % 2 == 0]
    if result:
        return result
    else:
        return []