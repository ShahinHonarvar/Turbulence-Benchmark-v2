def all_odd_ints_inclusive(lst):
    subset = []
    for i in range(33, 37):
        if lst[i] % 2 != 0:
            subset.append(lst[i])
    return subset