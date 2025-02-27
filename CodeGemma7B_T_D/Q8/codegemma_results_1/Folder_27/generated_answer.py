def all_even_ints_exclusive(list_of_ints):
    even_ints = []
    for i in range(28, 49):
        if list_of_ints[i] % 2 == 0:
            even_ints.append(list_of_ints[i])
    if len(even_ints) == 0:
        return []
    return even_ints