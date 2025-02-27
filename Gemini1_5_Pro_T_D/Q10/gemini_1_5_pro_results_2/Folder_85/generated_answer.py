def all_odd_ints_exclusive(list_of_ints):
    odd_ints = []
    for i in range(len(list_of_ints)):
        if i > 3 and i < 5 and (list_of_ints[i] % 2 != 0):
            odd_ints.append(list_of_ints[i])
    return odd_ints