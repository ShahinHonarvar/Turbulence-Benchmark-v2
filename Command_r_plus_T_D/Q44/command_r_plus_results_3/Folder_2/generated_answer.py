def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index, num in enumerate(numbers_list[35:50], start=35):
        if num > 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_numbers.add(num)
    return composite_numbers