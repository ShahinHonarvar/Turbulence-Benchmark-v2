def all_even_ints_inclusive(list_of_ints):
    even_ints = []
    if len(list_of_ints) >= 89:
        for i in range(22, 89):
            if list_of_ints[i] % 2 == 0:
                even_ints.append(list_of_ints[i])
    return even_ints