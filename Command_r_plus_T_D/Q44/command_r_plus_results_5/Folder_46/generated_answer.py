def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_nums = set()
    for idx in range(28, 39):
        if numbers_list[idx] <= 1:
            continue
        is_prime = all((numbers_list[idx] % i != 0 for i in range(2, int(numbers_list[idx] ** 0.5) + 1)))
        if not is_prime:
            composite_nums.add(numbers_list[idx])
    return composite_nums