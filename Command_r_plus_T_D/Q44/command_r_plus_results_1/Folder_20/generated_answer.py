def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[74:96], 74):
        if number > 1 and (not all((number % i for i in range(2, int(number ** 0.5) + 1)))):
            composite_numbers.add(number)
    return composite_numbers