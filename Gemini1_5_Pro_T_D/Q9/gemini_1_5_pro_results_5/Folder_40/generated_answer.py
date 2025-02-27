def all_odd_ints_inclusive(list_of_ints):
    odd_ints = []
    for i in range(0, 3):
        if i < len(list_of_ints) and list_of_ints[i] % 2 != 0:
            odd_ints.append(list_of_ints[i])
    return odd_ints