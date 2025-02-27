def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[20:201], start=20):
        if number > 1 and any((number % factor == 0 for factor in range(2, int(number ** 0.5) + 1))):
            composite_numbers.add(number)
    return composite_numbers