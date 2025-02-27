def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_set = set()
    for index, num in enumerate(numbers_list[29:80], start=29):
        if num <= 1:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                composite_set.add(num)
                break
    return composite_set