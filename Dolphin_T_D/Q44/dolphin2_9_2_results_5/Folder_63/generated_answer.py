def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(17, 79):
        if all((i % j != 0 for j in range(2, i))):
            composite_nums.add(i)
    return composite_nums