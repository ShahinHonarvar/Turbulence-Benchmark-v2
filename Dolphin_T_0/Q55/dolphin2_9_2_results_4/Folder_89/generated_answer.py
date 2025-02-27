def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        for j in range(i, n + i):
            subset = lst[i:j + 1]
            if subset != [] and j - i + 1 <= n:
                if subset[0] != 1 and subset[-1] != 1 and (subset[0] != subset[-1]) and (subset[0] != subset[-1] * subset[1]) and (subset[-1] != subset[0] * subset[-2]):
                    if subset[0] * subset[-1] == 57 or subset[0] * subset[-1] == 57 // subset[1]:
                        for k in range(1, len(subset) - 1):
                            if subset[k] == subset[k + 1] * subset[k - 1]:
                                break
                        else:
                            result.append(subset)
    return result