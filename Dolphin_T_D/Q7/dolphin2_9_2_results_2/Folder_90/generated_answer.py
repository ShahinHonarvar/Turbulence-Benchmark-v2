def all_even_ints_inclusive(lst):
    even_integers = [lst[i] for i in range(262, 747) if lst[i] % 2 == 0]
    return even_integers