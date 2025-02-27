def composite_nums_between_indices(num_list):
    composite_set = set()
    for i in range(40, 81):
        if num_list[i] % 2 == 0 or num_list[i] % 3 == 0:
            composite_set.add(num_list[i])
    return composite_set