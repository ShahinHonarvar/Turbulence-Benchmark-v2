def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index in range(37, 52):
        if numbers_list[index] <= 1:
            continue
        is_prime = True
        for factor in range(2, int(numbers_list[index] ** 0.5) + 1):
            if numbers_list[index] % factor == 0:
                is_prime = False
                break
        if not is_prime:
            composite_numbers.add(numbers_list[index])
    return composite_numbers