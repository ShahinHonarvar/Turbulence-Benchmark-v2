def lists_with_product_equal_n(lst):
    if len(lst) == 0:
        return []
    n = len(lst)
    index_map = {0: -1}
    product = 1
    for i in range(n):
        product *= lst[i]
        index_map[product] = i
    product_set = set()
    result = []
    for i in range(n):
        for j in range(i, n):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k]
            if product in index_map and index_map[product] > i:
                product_set.add(tuple(lst[i:j + 1]))
    if len(product_set) == 0:
        return []
    return [list(x) for x in product_set]