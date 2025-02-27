def all_even_ints_inclusive(list_of_ints):
    even_ints = []
    if len(list_of_ints) > 0:
        if list_of_ints[0] % 2 == 0:
            even_ints.append(list_of_ints[0])
    return even_ints