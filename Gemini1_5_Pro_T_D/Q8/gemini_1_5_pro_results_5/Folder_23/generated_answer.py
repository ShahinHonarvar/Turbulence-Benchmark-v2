def all_even_ints_exclusive(ints):
    even_ints = []
    for i in range(max(29, 0), min(53, len(ints))):
        if ints[i] % 2 == 0:
            even_ints.append(ints[i])
    return even_ints