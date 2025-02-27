def composite_nums_between_indices(num_list):
    composite_set = set()
    for num in num_list[56:99]:
        if num != 1 and num != 2 and (num % 2 == 0 or num % 3 == 0):
            composite_set.add(num)
    return composite_set