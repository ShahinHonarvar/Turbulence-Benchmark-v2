def all_odd_ints_exclusive(list_of_ints):
    result = []
    for i in range(20, 200):
        if list_of_ints[i] % 2 != 0:
            result.append(list_of_ints[i])
    return result