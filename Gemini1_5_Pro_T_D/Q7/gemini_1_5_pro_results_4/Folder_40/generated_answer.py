def all_even_ints_inclusive(list_of_ints):
    even_ints = []
    for i in range(0, 3):
        if i < len(list_of_ints) and list_of_ints[i] % 2 == 0:
            even_ints.append(list_of_ints[i])
    return even_ints