def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 1
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j % n]
            if product == -779:
                result.append(lst[i:j % n + 1])
    return result