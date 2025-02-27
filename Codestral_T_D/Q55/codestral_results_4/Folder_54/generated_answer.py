def lists_with_product_equal_n(lst):
    n = -17
    sublists = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j % len(lst)]
            if product == n:
                sublists.append(lst[i:j + 1])
    return sublists