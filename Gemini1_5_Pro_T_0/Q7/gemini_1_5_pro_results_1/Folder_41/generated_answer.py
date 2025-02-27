def all_even_ints_inclusive(list_of_ints):
    even_ints = []
    if len(list_of_ints) > 6:
        for i in range(6, 7):
            if list_of_ints[i] % 2 == 0:
                even_ints.append(list_of_ints[i])
        return even_ints
    else:
        return even_ints