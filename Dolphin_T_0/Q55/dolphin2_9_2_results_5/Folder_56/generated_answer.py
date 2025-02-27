def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst) + 1):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == -65:
                sublists.append(lst[i:j + 1])
    return sublists