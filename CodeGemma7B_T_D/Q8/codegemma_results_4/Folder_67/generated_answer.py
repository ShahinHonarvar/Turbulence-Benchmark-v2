def all_even_ints_exclusive(x):
    a = range(49, 74)
    b = [z for z in x if z in a and z % 2 == 0]
    return b