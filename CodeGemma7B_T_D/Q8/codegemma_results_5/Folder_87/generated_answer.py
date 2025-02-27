def all_even_ints_exclusive(list_of_ints):
    result = []
    for i in range(32, 99):
        if i % 2 == 0:
            result.append(list_of_ints[i])
    return result