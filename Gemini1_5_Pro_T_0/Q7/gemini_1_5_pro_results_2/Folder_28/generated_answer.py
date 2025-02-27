def all_even_ints_inclusive(list_of_ints):
    even_ints = []
    for i in range(max(0, min(62, len(list_of_ints) - 1)), min(63, len(list_of_ints)) + 1):
        if list_of_ints[i] % 2 == 0:
            even_ints.append(list_of_ints[i])
    return even_ints