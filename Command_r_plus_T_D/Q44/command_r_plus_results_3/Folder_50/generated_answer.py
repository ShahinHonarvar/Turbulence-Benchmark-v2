def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_nums_set = set()
    for num in numbers_list[56:58]:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_nums_set.add(num)
    return composite_nums_set