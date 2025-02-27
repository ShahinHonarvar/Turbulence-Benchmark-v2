def list_with_product_equal_n(lst):
    lst = lst + lst
    results = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            product = 1
            for k in range(i, j):
                product *= lst[k]
            if product == -56:
                results.append(lst[i:j])
    return results