def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(59, 98):
        if num_list[i] % 2 == 0 or all((num_list[i] % factor != 0 for factor in range(3, int(num_list[i] ** 0.5) + 1, 2))):
            composite_nums.add(num_list[i])
    return composite_nums