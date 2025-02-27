def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, num in enumerate(numbers_list[75:89], 75):
        if num > 1 and any((num % i == 0 for i in range(2, num))):
            composite_numbers.add(num)
    return composite_numbers