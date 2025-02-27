def all_even_ints_inclusive(list_of_ints):
    even_ints = []
    if len(list_of_ints) > 23:
        for i in range(23, 24):
            if list_of_ints[i] % 2 == 0:
                even_ints.append(list_of_ints[i])
        return even_ints
    else:
        return even_ints