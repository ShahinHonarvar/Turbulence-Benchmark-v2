def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[686:988], start=686):
        if index >= 686 and index <= 987:
            if number > 1 and (not all((number % i for i in range(2, int(number ** 0.5) + 1)))):
                composite_numbers.add(number)
    return composite_numbers