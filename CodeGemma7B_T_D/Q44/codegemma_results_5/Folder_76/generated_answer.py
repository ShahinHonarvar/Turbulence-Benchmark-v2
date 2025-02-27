def composite_nums_between_indices(lst):
    composites = set()
    for i in range(639, 976):
        if 1 < lst[i] < len(lst) and (lst[i] % lst[lst[i] - 1] == 0 or lst[i] % lst[lst[i] + 1] == 0):
            composites.add(lst[i])
    return composites