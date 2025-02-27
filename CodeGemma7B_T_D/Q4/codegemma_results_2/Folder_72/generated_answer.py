def all_pos_ints_exclusive(lst):
    output = []
    for i in range(56, 88):
        if lst[i] > 0:
            output.append(lst[i])
    if len(output) == 0:
        output = []
    return output