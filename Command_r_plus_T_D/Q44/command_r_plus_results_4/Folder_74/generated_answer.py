def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[42:69], start=42):
        if index >= 42 and index <= 68:
            if number > 1 and all((number % i != 0 for i in range(2, int(number ** 0.5) + 1))):
                composite_numbers.add(number)
    return composite_numbers