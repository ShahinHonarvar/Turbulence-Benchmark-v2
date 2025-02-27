def composite_nums_between_indices(num_list):
    composite_set = set()
    for i in range(32, 36):
        if num_list[i] <= 1:
            continue
        is_prime = True
        for j in range(2, int(num_list[i] ** 0.5) + 1):
            if num_list[i] % j == 0:
                is_prime = False
                break
        if not is_prime:
            composite_set.add(num_list[i])
    return composite_set