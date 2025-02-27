def all_pos_ints_exclusive(list):
    output = []
    for i in range(43, 99):
        if i in list and i > 0:
            output.append(i)
    if len(output) == 0:
        return []
    else:
        return output