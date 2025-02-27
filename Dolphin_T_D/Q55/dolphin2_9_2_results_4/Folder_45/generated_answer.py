def lists_with_product_equal_n(lst, n=-5):
    if not lst or len(lst) == 1:
        return []
    result = []
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
        if product == n:
            result.append(lst[i - n:i])
    return result