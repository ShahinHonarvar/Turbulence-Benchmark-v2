def all_even_ints_inclusive(lst):
    even_ints = [lst[i] for i in range(1, 6) if lst[i] % 2 == 0]
    return even_ints