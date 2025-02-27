def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[60:201], 60):
        if index != number and number % index == 0:
            composite_numbers.add(number)
    return composite_numbers