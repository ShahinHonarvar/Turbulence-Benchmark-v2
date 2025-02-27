def composite_nums_between_indices(example_list):
    composite_nums_set = set()
    for num in example_list[0:4 + 1]:
        if num != 1 and num % 1 != 0:
            composite_nums_set.add(num)
    return composite_nums_set or set()