def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for i in range(43, 52):
        if numbers_list[i] <= 1:
            continue
        is_prime = True
        for j in range(2, int(numbers_list[i] ** 0.5) + 1):
            if numbers_list[i] % j == 0:
                is_prime = False
                break
        if not is_prime:
            composite_set.add(numbers_list[i])
    return composite_set