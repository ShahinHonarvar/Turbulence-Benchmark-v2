def all_neg_ints_exclusive(list_of_ints):
    result = []
    for i in range(1, 3):
        if list_of_ints[i] < 0:
            result.append(list_of_ints[i])
    return result