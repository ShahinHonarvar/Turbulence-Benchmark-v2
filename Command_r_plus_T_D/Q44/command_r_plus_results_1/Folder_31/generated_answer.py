def composite_nums_between_indices(num_list: list[int]) -> set[int]:
    composite_nums = set()
    for i in range(56, 67):
        if num_list[i] <= 1:
            continue
        is_prime = all((num_list[i] % j != 0 for j in range(2, int(num_list[i] ** 0.5) + 1)))
        if not is_prime:
            composite_nums.add(num_list[i])
    return composite_nums