def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for index, num in enumerate(numbers_list[25:60], start=25):
        if num <= 1:
            continue
        for factor in range(2, int(num ** 0.5) + 1):
            if num % factor == 0:
                composite_set.add(num)
                break
    return composite_set