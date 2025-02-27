def composite_nums_between_indices(numbers_list):
    composite_set = set()
    for index, num in enumerate(numbers_list[:10]):
        if index != 0 and num % 2 == 0:
            composite_set.add(num)
    return composite_set