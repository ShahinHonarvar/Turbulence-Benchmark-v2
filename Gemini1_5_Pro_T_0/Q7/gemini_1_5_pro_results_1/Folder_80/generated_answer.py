def all_even_ints_inclusive(list_of_ints):
    even_ints = []
    for i in range(max(64, 0), min(len(list_of_ints), 67)):
        if list_of_ints[i] % 2 == 0:
            even_ints.append(list_of_ints[i])
    return even_ints