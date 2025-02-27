def all_even_ints_exclusive(list_of_ints):
    result = []
    for i in range(69, 97):
        if list_of_ints[i] % 2 == 0:
            result.append(list_of_ints[i])
    if not result:
        return []
    return result