def lists_with_product_equal_n(lst):
    n = len(lst)
    sublists = []
    product = 1
    for i in range(n):
        product *= lst[i]
        if product == 74:
            sublists.append(lst[:i + 1])
    if product != 74:
        sublists.append([])
    sublists_equal_product = []
    for i in range(1, n):
        product = lst[0]
        for j in range(1, i):
            product *= lst[j]
        if product == 74:
            sublists_equal_product.append(lst[0:i])
    sublists += sublists_equal_product
    sublists = list(map(list, set(map(tuple, sublists))))
    return sublists