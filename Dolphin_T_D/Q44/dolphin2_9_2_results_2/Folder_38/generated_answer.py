def composite_nums_between_indices(lst):
    result = set()
    for i in range(29, 94):
        if lst[i] > 1:
            for j in range(2, lst[i]):
                if lst[i] % j == 0:
                    result.add(lst[i])
                    break
    return result