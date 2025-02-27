def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for index, num in enumerate(numbers_list[22:64], start=22):
        if num > 1 and any((num % i == 0 for i in range(2, num))):
            composite_numbers.add(num)
    return composite_numbers