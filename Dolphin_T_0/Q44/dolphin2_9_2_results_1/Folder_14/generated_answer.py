def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(4, 5):
        if all((i % num != 0 for num in range(2, int(i ** 0.5) + 1))):
            composite_nums.add(i)
    return composite_nums