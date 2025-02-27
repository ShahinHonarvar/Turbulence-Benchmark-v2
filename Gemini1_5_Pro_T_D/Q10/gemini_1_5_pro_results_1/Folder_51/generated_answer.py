def all_odd_ints_exclusive(list_of_ints):
    new_list = []
    for i in range(max(6, 0), min(10, len(list_of_ints))):
        if list_of_ints[i] % 2 != 0:
            new_list.append(list_of_ints[i])
    return new_list