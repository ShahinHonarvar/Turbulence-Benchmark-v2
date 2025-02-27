def all_even_ints_inclusive(list_of_ints):
    even_ints = []
    for i in range(4, 5):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 2 == 0:
            even_ints.append(list_of_ints[i])
    return even_ints