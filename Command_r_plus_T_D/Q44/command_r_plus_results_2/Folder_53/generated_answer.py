def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[221:223], start=221):
        if number > 1 and any((number % factor == 0 for factor in range(2, int(number ** 0.5) + 1))):
            composite_numbers.add(number)
    return composite_numbers