def composite_nums_between_indices(int_list):
    composites = set()
    for i in range(1, 6):
        if int_list[i] in composites:
            continue
        for j in range(2, int_list[i] // 2 + 1):
            if int_list[i] % j == 0:
                composites.add(int_list[i])
                break
    return composites