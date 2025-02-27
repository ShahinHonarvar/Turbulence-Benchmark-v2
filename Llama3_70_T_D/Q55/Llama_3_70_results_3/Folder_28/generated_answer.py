def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product > 85:
                break
            if product == 85:
                result.append(lst[j % n] if j == i else lst[i:j % n + 1])
    return result