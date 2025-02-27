def composite_nums_between_indices(num_list):
    composite_set = set()
    for i in range(70, 85):
        num = num_list[i]
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            continue
        composite_set.add(num)
    return composite_set