def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for num in numbers_list[29:52]:
        if num > 1 and (not all((num % i for i in range(2, int(num ** 0.5) + 1)))):
            composite_set.add(num)
    return composite_set