def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(40, 201):
        if num_list[i] not in [x for x in range(2, int(num_list[i] ** 0.5) + 1) if num_list[i] % x == 0]:
            composite_nums.add(num_list[i])
    return composite_nums