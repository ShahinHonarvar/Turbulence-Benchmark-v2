def all_odd_ints_inclusive(list_of_ints):
    odd_ints = []
    for i in range(639, 976):
        if list_of_ints[i] % 2 != 0:
            odd_ints.append(list_of_ints[i])
    return odd_ints