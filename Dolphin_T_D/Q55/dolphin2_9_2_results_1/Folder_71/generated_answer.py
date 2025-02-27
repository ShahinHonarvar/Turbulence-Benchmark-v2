def lists_with_product_equal_n(lst):
    results = []
    n = len(lst)
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == 47:
                results.append(lst[i:i + j + 1])
    return results