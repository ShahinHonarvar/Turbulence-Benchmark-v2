def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_numbers = set()
    for num in numbers_list[82:87]:
        if num > 1 and all((num % i != 0 for i in range(2, num))):
            composite_numbers.add(num)
    return composite_numbers