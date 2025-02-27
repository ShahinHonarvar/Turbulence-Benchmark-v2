def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for index, num in enumerate(numbers_list[31:73], start=31):
        if num > 1 and any((num % factor == 0 for factor in range(2, num))):
            composite_set.add(num)
    return composite_set