def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[246:751], start=246):
        if index > 1 and all((number % factor != 0 for factor in range(2, int(number ** 0.5) + 1))):
            continue
        composite_numbers.add(number)
    return composite_numbers