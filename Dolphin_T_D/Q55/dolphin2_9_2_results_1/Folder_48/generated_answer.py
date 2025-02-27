def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 1
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == 990:
                result.append(lst[i:j + 1])
    return result