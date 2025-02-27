def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product = 1
    for i in range(n):
        if i > 0:
            product /= lst[i - 1]
        for j in range(i, n):
            if i == 0:
                product = lst[j]
            else:
                product *= lst[j]
            if product == 37:
                result.append(lst[i:j + 1])
    return result