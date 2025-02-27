def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for num in numbers_list[23:24]:
        if num <= 1:
            continue
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                composite_set.add(num)
                break
    return composite_set