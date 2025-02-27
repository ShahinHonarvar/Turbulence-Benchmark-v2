def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_set = set()
    for index, num in enumerate(numbers_list[13:69], start=13):
        if num > 1 and any((num % i == 0 for i in range(2, num))):
            composite_set.add(num)
    return composite_set