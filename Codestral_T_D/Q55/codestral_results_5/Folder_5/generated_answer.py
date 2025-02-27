def lists_with_product_equal_n(lst):
    n = len(lst)
    lst += lst
    result = []
    for i in range(n):
        for j in range(i, i + n):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k]
                if product == -33:
                    result.append(lst[i:j + 1])
    return result