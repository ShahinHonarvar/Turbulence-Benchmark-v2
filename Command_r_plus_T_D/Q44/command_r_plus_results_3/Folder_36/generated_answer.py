def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_set = set()
    for num in numbers_list[686:988]:
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            continue
        composite_set.add(num)
    return composite_set