def lists_with_product_equal_n(lst, n=54):
    result = []
    if len(lst) < 2:
        return result
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
        if product == n:
            result.append(lst[:i + 1])
        for j in range(i + 1, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            product /= lst[j - i]
    return result