def all_even_ints_inclusive(lst):
    result = [x for x in lst[13:69] if x % 2 == 0]
    return result if result else []