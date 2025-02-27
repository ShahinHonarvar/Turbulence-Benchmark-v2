def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[55:99], start=55):
        if index != number and number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    composite_numbers.add(number)
                    break
    return composite_numbers