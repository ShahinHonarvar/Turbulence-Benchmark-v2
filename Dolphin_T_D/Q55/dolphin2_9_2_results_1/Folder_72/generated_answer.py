def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    prefix_product = 1
    product_map = {1: [[]]}
    for i in range(n + 1):
        if i < n:
            prefix_product *= lst[i]
        for product, path in list(product_map.items()):
            if i < n and product * lst[i] not in product_map:
                product_map[product * lst[i]] = [p + [lst[i]] for p in list(path)]
    if n == 1 and lst[0] != 1:
        result.append([lst[0]])
    return result + product_map.get(10, [])