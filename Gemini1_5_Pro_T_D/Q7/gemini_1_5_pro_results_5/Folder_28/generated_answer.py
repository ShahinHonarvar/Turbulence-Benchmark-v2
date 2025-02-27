def all_even_ints_inclusive(list_of_ints):
    even_ints = []
    for i in range(max(62, 0), min(64, len(list_of_ints))):
        if list_of_ints[i] % 2 == 0:
            even_ints.append(list_of_ints[i])
    return even_ints