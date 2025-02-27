def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for index in range(14, 65):
        if numbers_list[index] <= 1:
            continue
        is_prime = all((numbers_list[index] % num != 0 for num in range(2, int(numbers_list[index] ** 0.5) + 1)))
        if not is_prime:
            composite_set.add(numbers_list[index])
    return composite_set