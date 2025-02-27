def all_even_ints_inclusive(ints):
    even_ints = [ints[i] for i in range(62, 64) if ints[i] % 2 == 0]
    if not even_ints:
        return []
    else:
        return even_ints