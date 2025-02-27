def lists_with_product_equal_n(lst):
    n = len(lst)
    product_target = 2
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == product_target:
                result.append(lst[i:j % n + 1])
    return result