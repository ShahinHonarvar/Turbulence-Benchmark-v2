def all_odd_ints_exclusive(list_in):
    odd_ints = []
    for i in range(71, 98):
        if i % 2 != 0 and i < len(list_in):
            odd_ints.append(list_in[i])
    return odd_ints