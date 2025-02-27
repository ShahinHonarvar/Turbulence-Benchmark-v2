def composite_nums_between_indices(lst):
    result = set()
    for i in range(70, 85):
        if i < len(lst) and (not lst[i] % 2 == 0) and (lst[i] > 1):
            result.add(lst[i])
    return result