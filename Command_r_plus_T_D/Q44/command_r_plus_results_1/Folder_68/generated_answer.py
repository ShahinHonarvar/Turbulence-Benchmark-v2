def composite_nums_between_indices(numbers_list: list[int]) -> set:
    composite_set = set()
    for index, num in enumerate(numbers_list[:9]):
        if index == 0 or index == 8:
            if num > 1:
                composite_set.add(num)
        elif num > 1 and (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or (num % 7 == 0)):
            composite_set.add(num)
    return composite_set