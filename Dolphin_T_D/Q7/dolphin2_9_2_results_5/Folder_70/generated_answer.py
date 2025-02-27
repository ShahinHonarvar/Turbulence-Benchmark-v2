def all_even_ints_inclusive(lst):
    even_ints = [lst[i] for i in range(28, 33) if lst[i] % 2 == 0]
    return even_ints if even_ints else []