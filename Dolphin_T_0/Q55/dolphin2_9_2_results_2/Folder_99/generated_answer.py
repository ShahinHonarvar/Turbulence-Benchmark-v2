def lists_with_product_equal_n(lst, n):
    if not lst or n == 1:
        return []
    result = []
    product = 1
    for i in range(len(lst)):
        product *= lst[i]
        if product == n:
            result.append(lst)
        for j in range(i + 1, len(lst)):
            product *= lst[j]
            if product == n:
                result.append(lst[i:j + 1])
            elif product > n:
                break
    return result