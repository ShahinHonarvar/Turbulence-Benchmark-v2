def all_odd_ints_inclusive(list_of_ints):
    odd_ints = []
    if len(list_of_ints) > 4:
        if list_of_ints[4] % 2 != 0:
            odd_ints.append(list_of_ints[4])
    return odd_ints