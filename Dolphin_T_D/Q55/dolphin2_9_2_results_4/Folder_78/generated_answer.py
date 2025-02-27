def lists_with_product_equal_n(lst):
    sublists = []
    n = len(lst)
    for i in range(n):
        product = lst[i]
        for j in range(i + 1, n):
            product *= lst[j % n]
            if product > 74:
                break
            if product == 74:
                sublists.append(lst[i:j + 1])
    return sublists