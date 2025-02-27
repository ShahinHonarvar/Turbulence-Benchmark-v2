def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, num in enumerate(numbers_list[70:201], 70):
        if index != num and num % index == 0:
            composite_numbers.add(num)
    return composite_numbers