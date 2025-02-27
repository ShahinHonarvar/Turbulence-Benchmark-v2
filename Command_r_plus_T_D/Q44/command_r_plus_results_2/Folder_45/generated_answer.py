def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index in range(40, 201):
        if numbers_list[index] <= 1:
            continue
        is_prime = all((numbers_list[index] % i != 0 for i in range(2, int(numbers_list[index] ** 0.5) + 1)))
        if not is_prime:
            composite_numbers.add(numbers_list[index])
    return composite_numbers