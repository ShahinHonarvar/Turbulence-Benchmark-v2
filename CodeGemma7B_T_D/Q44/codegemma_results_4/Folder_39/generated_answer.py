def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(62, 93):
        if num_list[i] > 1 and (not all((num_list[i] % j for j in range(2, int(num_list[i] ** 0.5) + 1)))):
            composite_nums.add(num_list[i])
    return composite_nums