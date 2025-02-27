def composite_nums_between_indices(lst):
    res = set()
    for i in lst[0:9]:
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    res.add(i)
    return res