def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for num in numbers_list[32:36]:
        if num > 1 and any((num % factor == 0 for factor in range(2, num))):
            composite_numbers.add(num)
    return composite_numbers