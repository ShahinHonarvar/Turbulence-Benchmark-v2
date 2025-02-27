def all_odd_ints_exclusive(list_of_ints):
    new_list = []
    for i in range(1, min(9, len(list_of_ints))):
        if list_of_ints[i] % 2 != 0:
            new_list.append(list_of_ints[i])
    return new_list