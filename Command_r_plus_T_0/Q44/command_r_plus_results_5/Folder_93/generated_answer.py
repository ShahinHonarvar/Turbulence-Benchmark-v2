def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for index in range(23, 24):
        if numbers_list[index] > 1 and (not all((numbers_list[index] % i for i in range(2, int(numbers_list[index] ** 0.5) + 1)))):
            composite_set.add(numbers_list[index])
    return composite_set