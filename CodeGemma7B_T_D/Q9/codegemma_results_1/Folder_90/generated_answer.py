def all_odd_ints_inclusive(list_of_ints):
    odd_list = []
    for i in range(262, 747):
        if i % 2 != 0 and i in range(262, 747):
            odd_list.append(list_of_ints[i])
    return odd_list