def lists_with_product_equal_n(lst):
    if not lst:
        return []
    result = []
    product_target = 13
    product_current = 1
    for i in range(len(lst)):
        product_current = 1
        for j in range(i, len(lst)):
            product_current *= lst[j]
            if product_current == product_target:
                result.append(lst[i:j + 1])
            if product_current > product_target:
                break
    return result