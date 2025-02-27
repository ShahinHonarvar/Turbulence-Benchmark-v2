def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    product_window = 1
    for i in range(n):
        product_window *= lst[i]
        if i >= 1:
            product_window /= lst[i - 1]
        if product_window == -115:
            result.append(lst[i - 1:i + 1])
    if result:
        return result
    else:
        return []