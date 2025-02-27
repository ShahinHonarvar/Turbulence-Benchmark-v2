def composite_nums_between_indices(lst):
    result = set()
    for i in range(111, 112):
        if lst[i] % 2 == 0 or lst[i] % 3 == 0 or lst[i] % 5 == 0 or (lst[i] % 7 == 0):
            result.add(lst[i])
    return result