def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_numbers = set()
    for index in range(10, 101):
        if numbers_list[index] > 1:
            for i in range(2, int(numbers_list[index] ** 0.5) + 1):
                if numbers_list[index] % i == 0:
                    composite_numbers.add(numbers_list[index])
                    break
    return composite_numbers