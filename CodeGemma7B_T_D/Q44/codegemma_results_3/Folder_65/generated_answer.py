def composite_nums_between_indices(lst):
    res = set()
    for i in range(82, 87):
        if i < len(lst):
            if lst[i] % 2 == 0 or lst[i] % 3 == 0:
                res.add(lst[i])
    return res