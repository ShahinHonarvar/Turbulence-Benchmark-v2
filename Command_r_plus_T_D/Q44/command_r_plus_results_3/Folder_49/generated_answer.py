def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[90:201], start=90):
        if index != 0 and number > 1 and all((number % i != 0 for i in range(2, int(number ** 0.5) + 1))):
            continue
        composite_numbers.add(number)
    return composite_numbers