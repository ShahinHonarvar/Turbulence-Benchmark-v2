def all_even_ints_exclusive(integers):
    even_integers = [x for i, x in enumerate(integers) if i in range(295, 573) and x % 2 == 0]
    return even_integers