def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(32, 36):
        if num_list[i] % 2 == 0 or num_list[i] % 3 == 0:
            composite_nums.add(num_list[i])
    return composite_nums