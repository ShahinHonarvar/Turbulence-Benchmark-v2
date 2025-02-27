def lists_with_product_equal_n(lst):
    lst = lst + lst
    result = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product = 1
            for k in range(i, j):
                product *= lst[k]
                if product == -837:
                    result.append(lst[i:k + 1])
    return result