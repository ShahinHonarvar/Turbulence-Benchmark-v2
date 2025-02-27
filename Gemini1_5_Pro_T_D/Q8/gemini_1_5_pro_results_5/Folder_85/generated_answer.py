def all_even_ints_exclusive(list_of_ints):
    even_ints = []
    for i in range(max(4, len(list_of_ints) - 1)):
        if i > 4 and i < len(list_of_ints) and (list_of_ints[i] % 2 == 0):
            even_ints.append(list_of_ints[i])
    return even_ints