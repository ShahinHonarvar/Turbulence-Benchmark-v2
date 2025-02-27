def all_even_ints_inclusive(lst):
    even_ints = [i for i in lst if i % 2 == 0]
    if even_ints:
        return even_ints[0:2]
    else:
        return []