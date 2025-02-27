def all_odd_ints_inclusive(list_of_ints):
    odd_ints = []
    for i in range(91, 100):
        if i >= len(list_of_ints):
            break
        if list_of_ints[i] % 2 != 0:
            odd_ints.append(list_of_ints[i])
    return odd_ints