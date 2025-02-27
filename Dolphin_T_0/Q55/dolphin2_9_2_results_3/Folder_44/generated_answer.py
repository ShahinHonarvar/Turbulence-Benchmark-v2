def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= lst[j]
            if product == 29:
                result.append(lst[i:j + 1])
            if product > 29:
                break
    return result