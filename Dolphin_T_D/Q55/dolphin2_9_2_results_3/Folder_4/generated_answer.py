def lists_with_product_equal_n(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            product = 1
            for k in range(i, j):
                product *= lst[k]
            if product == 91:
                return lst[i:j]
    return []