def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for index, num in enumerate(numbers_list[30:88], start=30):
        if num > 1 and any((num % i == 0 for i in range(2, num))):
            composite_set.add(num)
    return composite_set