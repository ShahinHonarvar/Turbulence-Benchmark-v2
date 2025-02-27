def lists_with_product_equal_n(lst):
    if not lst:
        return []
    n = len(lst)
    product = 1
    for i in range(n):
        if lst[i] == 0:
            return [[0]]
        product *= lst[i]
    target = -20
    if product != 1 and target % product != 0:
        return []
    target //= product
    sublists = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if j - i + 1 > n:
                break
            if product == target:
                sublists.append(lst[i:j % n + 1])
    return sublists