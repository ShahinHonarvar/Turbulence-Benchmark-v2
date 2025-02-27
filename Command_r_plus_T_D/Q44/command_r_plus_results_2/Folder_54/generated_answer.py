def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for i in range(14, 65):
        if numbers_list[i] <= 1:
            continue
        is_prime = True
        for j in range(2, int(numbers_list[i] ** 0.5) + 1):
            if numbers_list[i] % j == 0:
                is_prime = False
                break
        if not is_prime:
            composite_numbers.add(numbers_list[i])
    return composite_numbers