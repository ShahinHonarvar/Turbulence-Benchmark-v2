def composite_nums_between_indices(int_list):
    composites = set()
    for i in range(23, 24):
        if int_list[i] != 1 and int_list[i] % 2 == 0 and (int_list[i] % 3 == 0):
            composites.add(int_list[i])
    return composites