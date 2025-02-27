def all_even_ints_inclusive(lst):
    result = [i for i in lst[246:751] if i % 2 == 0]
    return result if result else []