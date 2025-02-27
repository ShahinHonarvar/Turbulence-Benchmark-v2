def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(51, 87):
        if lst[i] % 2 == 0 or lst[i] % 3 == 0:
            composite_nums.add(lst[i])
    return composite_nums