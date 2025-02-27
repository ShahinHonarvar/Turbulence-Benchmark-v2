def lists_with_product_equal_n(lst):
    results = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst)):
            product *= lst[j]
            if product > 537:
                break
            if product == 537:
                results.append(lst[i:j + 1])
    return results