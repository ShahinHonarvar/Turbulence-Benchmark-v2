def composite_nums_between_indices(lst):
    result = set()
    for i in range(40, 201):
        if all((i % j != 0 for j in range(2, i))):
            result.add(i)
    return result