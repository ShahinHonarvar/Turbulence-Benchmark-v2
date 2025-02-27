def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for index, num in enumerate(numbers_list[30:49], start=30):
        if num > 1 and (not all((num % i for i in range(2, int(num ** 0.5) + 1)))):
            composite_set.add(num)
    return composite_set