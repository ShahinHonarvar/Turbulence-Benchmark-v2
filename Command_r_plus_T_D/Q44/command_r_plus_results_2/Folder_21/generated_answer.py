def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, number in enumerate(numbers_list[262:747], start=262):
        if index != number and numbers_list.count(number) > 1:
            composite_numbers.add(number)
    return composite_numbers