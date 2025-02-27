def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[29:94], start=29):
        if index != number and numbers_list.count(number) > 1:
            composite_numbers.add(number)
    return composite_numbers