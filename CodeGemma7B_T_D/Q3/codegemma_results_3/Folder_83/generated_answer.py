def all_pos_ints_inclusive(lst):
    output = []
    for i in range(90, 201):
        if lst[i] > 0:
            output.append(lst[i])
    return output