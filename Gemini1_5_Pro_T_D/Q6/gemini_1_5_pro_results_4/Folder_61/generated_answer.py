def all_neg_ints_exclusive(list_of_ints):
    new_list = []
    for i in range(1, 7):
        if i < len(list_of_ints) and list_of_ints[i] < 0:
            new_list.append(list_of_ints[i])
    return new_list