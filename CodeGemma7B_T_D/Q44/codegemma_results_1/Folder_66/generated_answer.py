def composite_nums_between_indices(l):
    composite_nums = set()
    for i in range(62, 64):
        if l[i] % 2 == 0 or l[i] % 3 == 0 or l[i] % 5 == 0:
            composite_nums.add(l[i])
    return composite_nums