def lists_with_product_equal_n(lst):
    sublists = []
    n = 1
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product == 28:
                sublists.append(lst[i:j + 1])
    return sublists