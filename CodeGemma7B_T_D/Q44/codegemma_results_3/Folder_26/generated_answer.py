def composite_nums_between_indices(lst):
    composites = set()
    for i in range(22, 51):
        if lst[i] % 2 == 0 or lst[i] % 3 == 0:
            composites.add(lst[i])
    return composites