def all_neg_ints_exclusive(lst):
    output = []
    for i in range(23, 45):
        if lst[i] < 0:
            output.append(lst[i])
    return output