def all_neg_ints_inclusive(list_of_ints):
    result = []
    for i in range(min(len(list_of_ints), 7)):
        if list_of_ints[i] < 0:
            result.append(list_of_ints[i])
    return result