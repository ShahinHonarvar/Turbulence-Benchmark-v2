def composite_nums_between_indices(num_list):
    composite_nums = set()
    for i in range(56, 67):
        num = num_list[i]
        if all((num % j != 0 for j in range(2, int(num ** 0.5) + 1))):
            continue
        composite_nums.add(num)
    return composite_nums