def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index in range(70, 201):
        if numbers_list[index] <= 1:
            continue
        is_prime = True
        for num in range(2, int(numbers_list[index] ** 0.5) + 1):
            if numbers_list[index] % num == 0:
                is_prime = False
                break
        if not is_prime:
            composite_numbers.add(numbers_list[index])
    return composite_numbers