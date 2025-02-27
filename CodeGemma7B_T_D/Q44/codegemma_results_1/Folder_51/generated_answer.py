def composite_nums_between_indices(list):
    composites = set()
    for i in range(1, 9):
        if list[i] % 2 == 0 or (list[i] % 3 == 0 and list[i] != 3) or list[i] % 5 == 0 or (list[i] % 7 == 0 and list[i] != 7):
            composites.add(list[i])
    return composites