def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for idx in range(43, 52):
        if numbers_list[idx] > 1 and (not all((numbers_list[idx] % i for i in range(2, int(numbers_list[idx] ** 0.5) + 1)))):
            composite_set.add(numbers_list[idx])
    return composite_set