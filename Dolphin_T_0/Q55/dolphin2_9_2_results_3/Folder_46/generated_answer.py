def lists_with_product_equal_n(lst):
    n = len(lst)
    for i in range(n):
        prod = 1
        for j in range(i, i + n):
            prod = prod * lst[j % n]
            if prod == 53:
                return [lst[i:j]]
    return []