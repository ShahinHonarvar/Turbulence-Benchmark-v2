def composite_nums_between_indices(numbers_list):
    composite_set = set()
    for index, num in enumerate(numbers_list[:6]):
        if index != 0 and num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            composite_set.add(num)
    return composite_set