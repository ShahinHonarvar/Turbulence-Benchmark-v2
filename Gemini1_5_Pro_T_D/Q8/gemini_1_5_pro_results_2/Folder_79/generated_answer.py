def all_even_ints_exclusive(list_of_ints):
    even_ints = []
    for i in range(max(3, 0), min(8, len(list_of_ints))):
        if list_of_ints[i] % 2 == 0:
            even_ints.append(list_of_ints[i])
    return even_ints