def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[686:988], 687):
        if index == 687 or index == 987:
            if number > 1:
                composite_numbers.add(number)
        elif number > 1 and (number % 2 == 0 or number % 3 == 0 or number ** 0.5 % 1 == 0):
            composite_numbers.add(number)
    return composite_numbers