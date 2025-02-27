def composite_nums_between_indices(num_list):
    composites = set()
    for i in range(10, 101):
        if num_list[i] % 2 == 0 or num_list[i] % 3 == 0:
            composites.add(num_list[i])
    return composites