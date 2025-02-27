def lists_with_product_equal_n(lst):
    n = len(lst)
    product = 1
    sublists = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == 100:
                sublists.append(lst[i:i + j + 1])
    return sublists