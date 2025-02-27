def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_set = set()
    for index, num in enumerate(numbers_list[686:988], start=686):
        if index >= 686 and index <= 987:
            if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
                composite_set.add(num)
    return composite_set