def all_pos_ints_inclusive(lst):
    pos_numbers = []
    for i in range(28, 39):
        if lst[i] > 0:
            pos_numbers.append(lst[i])
    return pos_numbers