def composite_nums_between_indices(lst):
    composite_nums = set()
    for i in range(314, 348):
        if i != 1:
            for j in range(2, i):
                if i % j == 0:
                    composite_nums.add(lst[i])
                    break
    return composite_nums