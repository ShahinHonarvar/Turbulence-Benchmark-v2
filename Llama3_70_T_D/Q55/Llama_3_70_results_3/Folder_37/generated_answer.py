def lists_with_product_equal_n(lst):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            product = 1
            for k in range(i, j + 1):
                product *= lst[k]
            if product == -76:
                result.append(lst[i:j + 1])
        product = 1
        for j in range(len(lst)):
            product *= lst[(i + j) % len(lst)]
            if product == -76:
                result.append(lst[(i + j - len(lst) + 1) % len(lst):(i + j + 1) % len(lst)])
    return result