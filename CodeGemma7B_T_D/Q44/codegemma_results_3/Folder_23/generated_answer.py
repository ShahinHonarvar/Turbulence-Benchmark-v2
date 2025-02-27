def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(20, 31):
        if i >= len(num_list) or not isinstance(num_list[i], int):
            continue
        if num_list[i] % i == 0 and num_list[i] != i:
            composite_nums.add(num_list[i])
    return composite_nums