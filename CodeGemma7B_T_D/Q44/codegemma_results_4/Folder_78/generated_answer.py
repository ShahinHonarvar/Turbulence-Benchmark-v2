def composite_nums_between_indices(num_list):
    composites = set()
    for i in range(70, 85):
        if num_list[i] > 1 and all((num_list[i] % j for j in range(2, int(num_list[i] ** 0.5) + 1))):
            composites.add(num_list[i])
    return composites