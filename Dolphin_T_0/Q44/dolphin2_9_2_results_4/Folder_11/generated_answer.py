def composite_nums_between_indices(lst):
    cN = set()
    for i in range(37, 77):
        if all((i % j != 0 for j in range(2, i))):
            cN.add(lst[i])
    return cN