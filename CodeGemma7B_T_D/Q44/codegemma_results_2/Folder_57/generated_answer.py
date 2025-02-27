def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(25, 60):
        if lst[i] > 1 and (lst[i] % 2 == 0 or any((j % lst[i] == 0 for j in range(2, int(lst[i] ** (1 / 2)) + 1)))):
            composite_nums.add(lst[i])
    return composite_nums