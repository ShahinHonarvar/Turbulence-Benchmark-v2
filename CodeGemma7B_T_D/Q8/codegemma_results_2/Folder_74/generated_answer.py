def all_even_ints_exclusive(L):
    even_ints = [i for i in L[13:70] if i % 2 == 0]
    return even_ints if even_ints else []