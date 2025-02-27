def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for i in range(29, 94):
        if numbers_list[i] > 1 and (not all((numbers_list[i] % j for j in range(2, int(numbers_list[i] ** 0.5) + 1)))):
            composite_set.add(numbers_list[i])
    return composite_set