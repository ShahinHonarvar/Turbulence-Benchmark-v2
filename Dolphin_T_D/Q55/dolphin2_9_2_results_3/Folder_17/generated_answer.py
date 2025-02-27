def lists_with_product_equal_n(lst):
    res = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == 18:
                res.append(lst[i:j + 1])
        for j in range(i, i - len(lst), -1):
            product = 1
            for k in range(j, i - 1, -1):
                product *= lst[k]
            if product == 18:
                res.append(lst[j:i])
    return list(set((tuple(sorted(s)) for s in res)))