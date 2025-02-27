def all_even_ints_inclusive(lst):
    even_ints = [i for i in lst[36:47] if i % 2 == 0]
    return even_ints if len(even_ints) > 0 else []