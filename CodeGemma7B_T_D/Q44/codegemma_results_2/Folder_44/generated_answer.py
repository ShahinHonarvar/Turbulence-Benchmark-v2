def composite_nums_between_indices(int_list):
    composites = set()
    for i in range(64, 67):
        if int_list[i] != 1 and (not all((int_list[i] % j not in (0, 1) for j in range(2, int_list[i])))):
            composites.add(int_list[i])
    return composites