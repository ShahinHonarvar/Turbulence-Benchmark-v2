def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for num in numbers_list[34:56]:
        if num > 1 and any((num % factor == 0 for factor in range(2, int(num ** 0.5) + 1))):
            composite_numbers.add(num)
    return composite_numbers