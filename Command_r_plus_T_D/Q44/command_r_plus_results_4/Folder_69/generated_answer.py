def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for i in range(29, 80):
        if numbers_list[i] > 1:
            for j in range(2, int(numbers_list[i] ** 0.5) + 1):
                if numbers_list[i] % j == 0:
                    composite_set.add(numbers_list[i])
                    break
    return composite_set