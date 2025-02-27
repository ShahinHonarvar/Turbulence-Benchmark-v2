def composite_nums_between_indices(num_list):
    composites = set()
    for i in range(68, 87):
        if num_list[i] > 1 and sum((j for j in range(2, int(num_list[i] ** 0.5) + 1) if num_list[i] % j == 0)) > 1:
            composites.add(num_list[i])
    return composites