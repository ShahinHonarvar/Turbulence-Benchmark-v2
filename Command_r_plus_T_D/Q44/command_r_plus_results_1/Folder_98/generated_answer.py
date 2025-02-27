def composite_nums_between_indices(numbers_list):
    composite_set = set()
    for index, num in enumerate(numbers_list[:7]):
        if index in [0, 1, 6]:
            continue
        if num != 1 and all((num % i != 0 for i in range(2, num))):
            composite_set.add(num)
    return composite_set