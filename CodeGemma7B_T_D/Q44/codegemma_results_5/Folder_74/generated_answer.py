def composite_nums_between_indices(num_list):
    composites = set()
    for i in range(42, 69):
        if not num_list[i] % 2 and num_list[i] not in [4, 6, 8, 9] or (not num_list[i] % 3 and num_list[i] not in [9, 15]):
            composites.add(num_list[i])
    return composites