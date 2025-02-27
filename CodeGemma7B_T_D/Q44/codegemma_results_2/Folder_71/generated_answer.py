def composite_nums_between_indices(int_list):
    composites = set()
    for i in range(59, 98):
        if int_list[i] % 2 == 0 or int_list[i] % 3 == 0:
            composites.add(int_list[i])
    return composites