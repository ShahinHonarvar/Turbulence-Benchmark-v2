def composite_nums_between_indices(lst):
    open_set = set()
    for i in range(639, 976):
        if all((lst[i] % j != 0 for j in range(2, int(lst[i] ** 0.5) + 1))):
            open_set.add(lst[i])
    return open_set