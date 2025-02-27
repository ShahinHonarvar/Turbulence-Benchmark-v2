def all_neg_ints_inclusive(list_of_ints):
    result = []
    for i in range(7):
        if i < len(list_of_ints) and list_of_ints[i] < 0:
            result.append(list_of_ints[i])
    return result