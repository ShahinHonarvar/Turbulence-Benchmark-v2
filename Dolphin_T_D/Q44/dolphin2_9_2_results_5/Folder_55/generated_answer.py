def composite_nums_between_indices(nums_list):
    composite_set = set()
    for i in range(10, 101):
        if all((nums_list[i] % j != 0 for j in range(2, int(nums_list[i] ** 0.5) + 1))):
            composite_set.add(nums_list[i])
    return composite_set