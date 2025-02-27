def all_pos_ints_inclusive(lst):
    solution = []
    for i in range(29, 52):
        if lst[i] > 0:
            solution.append(lst[i])
    return solution