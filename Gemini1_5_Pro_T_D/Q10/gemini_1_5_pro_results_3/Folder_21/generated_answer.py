def all_odd_ints_exclusive(ints):
    odd_ints = []
    for i in range(744, 867):
        if i >= len(ints):
            break
        if ints[i] % 2 != 0:
            odd_ints.append(ints[i])
    return odd_ints