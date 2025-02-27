def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= lst[j % n]
            if product > 415:
                break
            if product == 415:
                result.append(lst[i:j] + lst[j % n:i])
    return result if result else []