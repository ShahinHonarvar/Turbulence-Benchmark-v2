def all_even_ints_exclusive(list_of_ints):
    even_ints = []
    for i in range(79, 93):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 2 == 0:
            even_ints.append(list_of_ints[i])
    return even_ints