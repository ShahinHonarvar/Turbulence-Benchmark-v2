def all_even_ints_inclusive(lst):
    result = [x for x in lst[68:87] if x % 2 == 0]
    return result if any(result) else []