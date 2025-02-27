def lists_with_product_equal_n(lst):
    size = len(lst)
    sublists = []
    for i in range(size):
        for j in range(i + 1, size + 1):
            product = 1
            for k in range(i, j):
                product *= lst[k]
            if product == 96:
                sublists.append(lst[i:j])
    return sublists