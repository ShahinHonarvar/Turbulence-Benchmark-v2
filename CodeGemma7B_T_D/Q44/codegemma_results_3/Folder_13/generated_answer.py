def composite_nums_between_indices(list):
    composites = set()
    for i in range(21, 98):
        if list[i] % 2 == 0:
            composites.add(list[i])
        elif list[i] % 3 == 0:
            composites.add(list[i])
        elif list[i] % 5 == 0:
            composites.add(list[i])
        elif list[i] % 7 == 0:
            composites.add(list[i])
    return composites