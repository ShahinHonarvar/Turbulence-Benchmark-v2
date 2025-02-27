def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j % n]
            if product == 4:
                sublists.append(lst[i:j + 1])
            if product > 4:
                break
    return sublists