def composite_nums_between_indices(l):
    result = set()
    for i in range(74, 96):
        if i < len(l):
            if l[i] > 1:
                for j in range(2, l[i]):
                    if l[i] % j == 0:
                        result.add(l[i])
                        break
    return result