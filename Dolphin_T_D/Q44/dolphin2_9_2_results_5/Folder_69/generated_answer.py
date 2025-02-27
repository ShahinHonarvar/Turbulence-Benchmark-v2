def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(29, 80):
        if not all((lst[i] % p for p in range(2, int(lst[i] ** 0.5) + 1))):
            composite_nums.add(lst[i])
    return composite_nums