def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[17:79], start=17):
        if index != number and numbers_list.count(number) > 1:
            composite_numbers.add(number)
    return composite_numbers