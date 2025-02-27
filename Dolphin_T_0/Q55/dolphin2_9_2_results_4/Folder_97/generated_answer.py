def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product == -938:
                sublists.append(lst[i:j + 1])
            if product - 938:
                break
    return sublists