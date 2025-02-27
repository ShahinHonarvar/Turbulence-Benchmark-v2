def all_odd_ints_inclusive(list_of_ints):
    new_list = []
    if len(list_of_ints) > 6:
        if list_of_ints[6] % 2 != 0:
            new_list.append(list_of_ints[6])
    return new_list