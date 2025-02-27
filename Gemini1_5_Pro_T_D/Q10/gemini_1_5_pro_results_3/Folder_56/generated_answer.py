def all_odd_ints_exclusive(list_of_ints):
    odd_ints = []
    for i in range(8, 9):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 2 != 0:
            odd_ints.append(list_of_ints[i])
    return odd_ints