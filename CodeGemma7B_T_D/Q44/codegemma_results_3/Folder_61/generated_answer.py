def composite_nums_between_indices(l):
    composites = set()
    for i in range(0, 8):
        if l[i] > 1 and all((l[i] % j != 0 for j in range(2, int(l[i] ** 0.5) + 1))):
            composites.add(l[i])
    return composites