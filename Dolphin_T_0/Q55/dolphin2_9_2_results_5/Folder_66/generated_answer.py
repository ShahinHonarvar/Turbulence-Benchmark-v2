def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    sublists = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product == 78:
                sublists.append(lst[i:j + 1])
    for i in range(n):
        product = 1
        for j in range(i, -1, -1):
            product *= lst[j]
            if product == 78:
                sublists.append(lst[j:i + 1])
    return list(set((tuple(sorted(sublist)) for sublist in sublists)))