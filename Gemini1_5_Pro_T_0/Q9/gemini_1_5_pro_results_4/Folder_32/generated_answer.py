def all_odd_ints_inclusive(ints):
    odd_ints = []
    for i in range(21, 98):
        if i in range(len(ints)) and ints[i] % 2 != 0:
            odd_ints.append(ints[i])
    return odd_ints