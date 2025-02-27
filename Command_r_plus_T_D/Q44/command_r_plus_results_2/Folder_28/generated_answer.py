def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_nums = set()
    for index, num in enumerate(numbers_list[22:89], start=22):
        if num > 1 and any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_nums.add(num)
    return composite_nums