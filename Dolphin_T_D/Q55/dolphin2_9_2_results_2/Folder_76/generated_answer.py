def product_equal_n(lst, n):
    size = len(lst)
    sublists = []
    for i in range(size):
        for j in range(i + 1, size + 1):
            product = 1
            for k in range(i, j):
                product *= lst[k]
            if product == n:
                sublists.append(lst[i:j])
    sublists.extend(sublists[-1] + sublists[:-1])
    return sublists

def lists_with_product_equal_n(lst):
    return product_equal_n(lst, 247)