def all_even_ints_inclusive(lst):
    even_ints = [i for i in lst[26:53] if i % 2 == 0]
    return even_ints if even_ints else []