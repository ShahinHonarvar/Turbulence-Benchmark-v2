def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_set = set()
    for i in range(59, 98):
        num = numbers_list[i]
        if num <= 1:
            continue
        for j in range(2, int(num ** 0.5) + 1):
            if num % j == 0:
                composite_set.add(num)
                break
    return composite_set