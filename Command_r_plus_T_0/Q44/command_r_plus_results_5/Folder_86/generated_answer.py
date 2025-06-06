def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_nums = set()
    for num in numbers_list[43:87]:
        if num > 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_nums.add(num)
    return composite_nums