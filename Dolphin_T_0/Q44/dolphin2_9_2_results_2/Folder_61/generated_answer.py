def composite_nums_between_indices(lst):
    result = set()
    for i in range(0, 7):
        if lst[i] > 1:
            for j in range(2, int(lst[i] ** 0.5) + 1):
                if lst[i] % j == 0:
                    result.add(lst[i])
                    break
    return result