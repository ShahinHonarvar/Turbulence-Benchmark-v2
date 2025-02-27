def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for i in range(59, 98):
        num = numbers_list[i]
        if num > 1 and any((num % j == 0 for j in range(2, int(num ** 0.5) + 1))):
            composite_numbers.add(num)
    return composite_numbers