def composite_nums_between_indices(lst):
    set1 = set()
    for i in range(64, 67):
        if lst[i] % 2 == 0 or lst[i] % 3 == 0:
            set1.add(lst[i])
    return set1