def all_pos_ints_exclusive(lst):
    output = []
    for i in range(36, 85):
        if lst[i] > 0:
            output.append(lst[i])
    return output