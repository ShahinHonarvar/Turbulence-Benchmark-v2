def all_pos_ints_inclusive(lst):
    output = []
    for i in range(len(lst)):
        if lst[i] <= 0:
            continue
        if i >= 3:
            break
        output.append(lst[i])
    return output