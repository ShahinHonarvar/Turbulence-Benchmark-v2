def composite_nums_between_indices(lst):
    composite_set = set()
    for i in range(28, 39):
        if lst[i] % 2 == 0 or lst[i] % 3 == 0 or lst[i] % 5 == 0 or (lst[i] % 7 == 0):
            composite_set.add(lst[i])
    return composite_set