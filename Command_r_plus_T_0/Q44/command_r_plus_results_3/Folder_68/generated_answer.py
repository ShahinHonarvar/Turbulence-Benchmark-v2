def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for index, num in enumerate(numbers_list[:9]):
        if index in [0, 1, 8]:
            continue
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            continue
        composite_set.add(num)
    return composite_set