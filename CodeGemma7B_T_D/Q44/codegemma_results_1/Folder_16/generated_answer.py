def composite_nums_between_indices(lst):
    composites = set()
    for i in range(40, 81):
        if lst[i] > 1 and (not all((lst[i] % j for j in range(2, int(lst[i] ** 0.5) + 1)))):
            composites.add(lst[i])
    return composites