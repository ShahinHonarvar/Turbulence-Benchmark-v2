def lists_with_product_equal_n(lst):
    size = len(lst)
    sublists = []
    for i in range(size):
        product = 1
        for j in range(i, size):
            product *= lst[j]
            if product == 247:
                sublists.append(lst[i:j + 1])
    return sublists