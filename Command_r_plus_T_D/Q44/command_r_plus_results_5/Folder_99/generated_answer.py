def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_set = set()
    for index in range(246, 751):
        current_num = numbers_list[index]
        if current_num <= 1:
            continue
        for divisor in range(2, int(current_num ** 0.5) + 1):
            if current_num % divisor == 0:
                composite_set.add(current_num)
                break
    return composite_set