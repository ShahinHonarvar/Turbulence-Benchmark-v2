def composite_nums_between_indices(numbers_list: list[int]) -> set[int]:
    composite_set = set()
    for index in range(19, 93):
        num = numbers_list[index]
        if num > 1 and any((num % i == 0 for i in range(2, num))):
            composite_set.add(num)
    return composite_set