def all_pos_ints_inclusive(lst):
    positive_ints = []
    for i in range(40, 81):
        if i < len(lst) and lst[i] > 0:
            positive_ints.append(lst[i])
    return positive_ints