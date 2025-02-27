def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for index, number in enumerate(numbers_list[56:99], start=56):
        if index != number and numbers_list.count(number) > 1:
            composite_set.add(number)
    return composite_set