def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product == 4:
                result.append(lst[i:j % n + 1])
            if product >= 4:
                break
    return result