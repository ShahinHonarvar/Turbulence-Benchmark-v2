def all_odd_ints_inclusive(list_of_ints):
    odd_ints = []
    for i in range(40, 201):
        if list_of_ints[i] % 2 == 1:
            odd_ints.append(list_of_ints[i])
    return odd_ints