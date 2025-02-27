def composite_nums_between_indices(num_list):
    composite_set = set()
    for i in range(37, 77):
        if num_list[i] != 1 and num_list[i] % 2 == 0:
            composite_set.add(num_list[i])
        for j in range(3, int(num_list[i] ** 0.5) + 1):
            if num_list[i] % j == 0:
                composite_set.add(num_list[i])
                break
    return composite_set