def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(1, 9):
        if i < len(lst) and lst[i] > 1 and (not lst[i] % 2 == 0) and (not lst[i] % 3 == 0):
            composite_nums.add(lst[i])
    return composite_nums