def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(40, 201):
        if num_list[i] != 1 and num_list[i] != 2 and (i % num_list[i] == 0):
            composite_nums.add(num_list[i])
    return composite_nums