def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    lst += lst
    for i in range(n):
        product = 1
        for j in range(i, i + n):
            product *= lst[j]
            if product == -82:
                result.append(lst[i:j + 1])
    return [x for x in result if len(x) <= n]