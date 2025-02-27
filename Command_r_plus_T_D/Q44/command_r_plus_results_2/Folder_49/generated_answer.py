def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_set = set()
    for index, num in enumerate(numbers_list[90:201], start=90):
        if index != num and num % index == 0:
            composite_set.add(num)
    return composite_set